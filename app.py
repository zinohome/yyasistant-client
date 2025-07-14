#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: ibmzhangjun@139.com
@file: app.py.py
@time: 2025/7/13 下午8:15
@desc: 
"""
import base64
import os
import io
import wave
import numpy as np
import audioop

from chainlit.input_widget import Switch
from config import config_from_dotenv
from utils.logger import logger
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cfg = config_from_dotenv(os.path.join(BASE_DIR, '.env'), read_from_file=True)

PROFILE_NAME = "健康助手"
PROFILE_ICON = "/public/profileimg/XiaoYan2.png"
PROFILE_DESC = "我是您的健康助手小研，我总是在这里，随时准备帮助您。我能够为您提供多方面、个性化的服务。"
PROFILE_STARTERS = [
    {
        "label": "健康与养生",
        "message": "给我介绍一些健康和养生方面的知识。",
        "icon": "/public/startterimg/chat.png"
    },
    {
        "label": "文艺与文化生活",
        "message": "退休后如何丰富文艺和文化生活？",
        "icon": "/public/startterimg/report.png"
    },
    {
        "label": "日常生活助手",
        "message": "做我的小助手，陪我聊天解闷。",
        "icon": "/public/startterimg/knowledge.png"
    },
    {
        "label": "新技能学习",
        "message": "退休后我可以学哪些新技能，给我推荐几个吧。",
        "icon": "/public/startterimg/doctor.png"
    },
]

# Define a threshold for detecting silence and a timeout for ending a turn
SILENCE_THRESHOLD = (
    3500  # Adjust based on your audio level (e.g., lower for quieter audio)
)
SILENCE_TIMEOUT = 1300.0  # Seconds of silence to consider the turn finished

import chainlit as cl
from utils.yyassistantapiclient import YYAssistantAPIClient


@cl.set_chat_profiles
async def chat_profile(current_user: cl.User):
    starters = [
        cl.Starter(label=s["label"], message=s["message"], icon=s["icon"])
        for s in PROFILE_STARTERS
    ]
    return [
        cl.ChatProfile(
            name=PROFILE_NAME,
            icon=PROFILE_ICON,
            markdown_description=PROFILE_DESC,
            starters=starters,
        )
    ]

@cl.on_chat_start
async def start():
    settings = await cl.ChatSettings(
        [
            Switch(id="auto_play_audio", label="自动播放语音", default=True, description="开启后会自动播报助手的语音回复"),
        ]
    ).send()
    await settings_update(settings)
@cl.on_settings_update
async def settings_update(settings):
    cl.user_session.set("chat_settings", settings)
@cl.on_chat_start
async def start_chat():
    # 初始化客户端和会话
    base_url = cfg.SERVER_BASE_URL
    client = YYAssistantAPIClient(base_url)  # 请替换为实际的API基础URL
    # 获取默认引擎
    default_engine = cfg.DEFAULT_AGENT_ENGINE
    if not default_engine:
        default_engine = await client.get_default_agent_engine()

    default_asr_engine = cfg.DEFAULT_ASR_ENGINE
    if not default_asr_engine:
        default_asr_engine = await client.get_default_asr_engine()

    default_tts_engine = cfg.DEFAULT_TTS_ENGINE
    if not default_tts_engine:
        default_tts_engine = await client.get_default_tts_engine()

    # 创建新会话
    conversation = await client.create_agent_conversation(default_engine, {"input": "开始对话"})
    conversation_id = conversation.get("data", "") if isinstance(conversation, dict) else ""

    # 存储客户端和会话ID到用户会话中
    cl.user_session.set("client", client)
    cl.user_session.set("conversation_id", conversation_id)
    cl.user_session.set("engine_name", default_engine)
    cl.user_session.set("asr_engine", default_asr_engine)
    cl.user_session.set("tts_engine", default_tts_engine)
    '''
    # 发送欢迎消息
    welcome_msg = f"您好，我是您的健康助手**{PROFILE_NAME}** 😊\n\n"
    welcome_msg += f"{PROFILE_DESC}\n\n"
    welcome_msg += "您可以直接输入问题，也可以点击左侧的快捷问题与我交流～\n\n"
    welcome_msg += "**以下是一些您可以尝试的问题：**\n"
    for idx, s in enumerate(PROFILE_STARTERS, 1):
        welcome_msg += f"{idx}. **{s['label']}**：{s['message']}\n"

    await cl.Message(content=welcome_msg).send()
    '''

# ASR处理——处理从@cl.on_audio_chunk来的音频转文字
async def asr_file_to_text(client, engine: str, audio_bytes: bytes, sample_rate=24000, sample_width=2):
    # 不处理MP3，直接WAV PCM处理
    data_b64 = base64.b64encode(audio_bytes[1]).decode("utf-8")  # 你接口asr_inference_wav的data直接传bytes
    #logger.info(f"asr_file_to_text data_b64: {data_b64}")
    asr_result = await client.asr_inference_wav(
        data=data_b64,
        user_id="chainlit-asr",
        engine=engine
    )
    # 按你接口返回的json处理
    if asr_result and isinstance(asr_result, dict) and "data" in asr_result:
        return asr_result["data"]
    elif asr_result and "text" in asr_result:
        return asr_result["text"]
    else:
        return ""


async def tts_text_to_speech(client, engine: str, text: str, max_len=150):
    # 按字符切片，不会截断中文
    text_list = [text[i:i + max_len] for i in range(0, len(text), max_len)]
    audio_bytes_segments = []

    for seg_text in text_list:
        tts_result = await client.tts_inference(
            data=seg_text,
            user_id="chainlit-tts",
            engine=engine
        )
        if tts_result and isinstance(tts_result, dict) and "data" in tts_result:
            audio_bytes = base64.b64decode(tts_result["data"])
            audio_bytes_segments.append(audio_bytes)

    return b"".join(audio_bytes_segments)

@cl.on_audio_start
async def on_audio_start():
    cl.user_session.set("audio_chunks", [])
    cl.user_session.set("silent_duration_ms", 0)
    cl.user_session.set("last_elapsed_time", 0)
    cl.user_session.set("is_speaking", False)
    return True


@cl.on_audio_chunk
async def on_audio_chunk(chunk: cl.InputAudioChunk):
    audio_chunks = cl.user_session.get("audio_chunks")
    if audio_chunks is None:
        audio_chunks = []
        cl.user_session.set("audio_chunks", audio_chunks)

    # 转为numpy方便后续拼接
    audio_chunk = np.frombuffer(chunk.data, dtype=np.int16)
    audio_chunks.append(audio_chunk)

    if chunk.isStart:
        cl.user_session.set("last_elapsed_time", chunk.elapsedTime)
        cl.user_session.set("is_speaking", True)
        return

    last_elapsed_time = cl.user_session.get("last_elapsed_time")
    if last_elapsed_time is None:
        last_elapsed_time = 0
    silent_duration_ms = cl.user_session.get("silent_duration_ms")
    if silent_duration_ms is None:
        silent_duration_ms = 0
    is_speaking = cl.user_session.get("is_speaking")
    cl.user_session.set("last_elapsed_time", chunk.elapsedTime)

    audio_energy = audioop.rms(chunk.data, 2)
    if audio_energy < SILENCE_THRESHOLD:
        silent_duration_ms += (chunk.elapsedTime - last_elapsed_time)
        cl.user_session.set("silent_duration_ms", silent_duration_ms)
        if silent_duration_ms > SILENCE_TIMEOUT and is_speaking:
            cl.user_session.set("is_speaking", False)
            await process_audio_input()
    else:
        # reset silence
        cl.user_session.set("silent_duration_ms", 0)
        if not is_speaking:
            cl.user_session.set("is_speaking", True)


async def process_audio_input():
    # 合并所有audio_chunks，转WAV
    audio_chunks = cl.user_session.get("audio_chunks")
    if not audio_chunks or not len(audio_chunks):
        cl.user_session.set("audio_chunks", [])
        return
    concatenated = np.concatenate(audio_chunks)
    wav_buffer = io.BytesIO()
    with wave.open(wav_buffer, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(24000)
        wav_file.writeframes(concatenated.tobytes())
    wav_buffer.seek(0)
    '''
    frames = wav_file.getnframes()
    rate = wav_file.getframerate()
    duration = frames / float(rate)
    if duration <= 1.71:
        logger.debug("The audio is too short, please try again.")
        return
    '''
    audio_buffer = wav_buffer.getvalue()
    whisper_input = ("audio.wav", audio_buffer, "audio/wav")
    client: YYAssistantAPIClient = cl.user_session.get("client")
    asr_engine = cl.user_session.get("asr_engine")

    transcription = await asr_file_to_text(
        client,
        engine=asr_engine,
        audio_bytes=whisper_input
    )

    cl.user_session.set("audio_chunks", [])

    # 回显原音频和文本
    input_audio_el = cl.Audio(content=wav_buffer.getvalue(), mime="audio/wav")
    # 顺带未来对齐，发送消息流
    await cl.Message(
        author='您',
        type="user_message",
        content=transcription,
        elements=[input_audio_el],
        metadata={"from_audio": True},
    ).send()

    # 直接把文字“发”给on_message逻辑
    await main(cl.Message(author='您', content=transcription,metadata={"from_audio": True}))

@cl.on_message
async def main(message: cl.Message):
    # 从用户会话中获取客户端和会话ID
    client: YYAssistantAPIClient = cl.user_session.get("client")
    conversation_id = cl.user_session.get("conversation_id")
    engine_name = cl.user_session.get("engine_name")
    tts_engine = cl.user_session.get("tts_engine")
    asr_engine = cl.user_session.get("asr_engine")

    if not client or not conversation_id:
        await cl.Message(content="会话未初始化，请刷新页面重试。", author="健康助手").send()
        return

    # 提前判断消息是否来源于语音
    from_audio = False
    meta = getattr(message, "metadata", None)
    if meta and isinstance(meta, dict):
        from_audio = meta.get("from_audio", False)

    # 读取 ChatSettings 设置
    chat_settings = cl.user_session.get("chat_settings") or {}
    auto_play_audio = chat_settings.get("auto_play_audio", True)  # 默认为True

    # 输出空消息用于流式token输出
    msg = cl.Message(content="", author="健康助手")
    await msg.send()

    # 调用 Agent 推理 API获取流式响应
    try:
        full_response = ""
        # 接收流式响应
        # ------ 新增try锁定generator -------
        stream_gen = client.agent_inference_stream(
            data=message.content,
            conversation_id=conversation_id,
            user_id="chainlit-user"
        )
        async for chunk in stream_gen:
            full_response += chunk
            await msg.stream_token(chunk)
        msg.content = full_response
        await msg.update()

        # 只在 from_audio 时边生成边TTS，同时分句更自然
        if from_audio and auto_play_audio and full_response.strip():
            tts_bytes = await tts_text_to_speech(client, tts_engine, full_response)
            if tts_bytes:
                audio_el = cl.Audio(content=tts_bytes, mime="audio/wav", auto_play=True)
                await cl.Message(content='', elements=[audio_el], author="健康助手").send()

    except Exception as e:
        # 创建新消息显示错误，而不是更新原有消息
        await cl.Message(author="健康助手", content=f"错误: {str(e)}").send()
        raise

if __name__ == "__main__":
    from chainlit.cli import run_chainlit
    run_chainlit(__file__)