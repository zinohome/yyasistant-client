#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: ibmzhangjun@139.com
@file: yyassistantapiclient.py
@time: 2025/7/13 下午6:06
@desc: 
"""
import os

import requests
from config import config_from_dotenv

from utils.logger import logger
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg = config_from_dotenv(os.path.join(BASE_DIR, '.env'), read_from_file=True)

class YYAssistantAPIClient:
    def __init__(self, base_url):
        self.base_url = cfg.SERVER_BASE_URL

    def get_asr_engine_list(self):
        """
        获取 ASR 支持引擎列表
        """
        url = f"{self.base_url}/yyh/asr/v0/engine"
        response = requests.get(url)
        return response.json()

    def asr_inference_wav(self, data, user_id="tester", request_id="", cookie="", **kwargs):
        """
        执行 ASR 引擎（wav 二进制）
        """
        url = f"{self.base_url}/yyh/asr/v0/engine"
        headers = {
            "User-Id": user_id,
            "Request-Id": request_id,
            "Cookie": cookie
        }
        payload = {
            "data": data,
            **kwargs
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    def get_default_asr_engine(self):
        """
        获取默认 ASR 引擎
        """
        url = f"{self.base_url}/yyh/asr/v0/engine/default"
        response = requests.get(url)
        return response.json()

    def get_asr_engine_param(self, engine):
        """
        获取 ASR 引擎配置参数列表
        """
        url = f"{self.base_url}/yyh/asr/v0/engine/{engine}"
        response = requests.get(url)
        return response.json()

    def asr_inference_mp3(self, file_path, engine, audio_type, config, sample_rate, sample_width, user_id="tester",
                          request_id="", cookie=""):
        """
        执行 ASR 引擎（mp3 文件）
        """
        url = f"{self.base_url}/yyh/asr/v0/engine/file"
        headers = {
            "User-Id": user_id,
            "Request-Id": request_id,
            "Cookie": cookie
        }
        with open(file_path, 'rb') as file:
            files = {
                "file": file
            }
            data = {
                "engine": engine,
                "type": audio_type,
                "config": config,
                "sampleRate": sample_rate,
                "sampleWidth": sample_width
            }
            response = requests.post(url, headers=headers, files=files, data=data)
        return response.json()

    def get_tts_engine_list(self):
        """
        获取 TTS 支持引擎列表
        """
        url = f"{self.base_url}/yyh/tts/v0/engine"
        response = requests.get(url)
        return response.json()

    def tts_inference(self, data, user_id="tester", request_id="", cookie="", **kwargs):
        """
        执行 TTS 引擎
        """
        url = f"{self.base_url}/yyh/tts/v0/engine"
        headers = {
            "User-Id": user_id,
            "Request-Id": request_id,
            "Cookie": cookie
        }
        payload = {
            "data": data,
            **kwargs
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    def get_default_tts_engine(self):
        """
        获取默认 TTS 引擎
        """
        url = f"{self.base_url}/yyh/tts/v0/engine/default"
        response = requests.get(url)
        return response.json()

    def get_tts_engine_voice_list(self, engine):
        """
        获取 TTS 引擎配置参数列表
        """
        url = f"{self.base_url}/yyh/tts/v0/engine/{engine}/voice"
        response = requests.get(url)
        return response.json()

    def get_tts_engine_param(self, engine):
        """
        获取 TTS 引擎配置参数列表
        """
        url = f"{self.base_url}/yyh/tts/v0/engine/{engine}"
        response = requests.get(url)
        return response.json()

    def get_llm_engine_list(self):
        """
        获取 LLM 支持引擎列表
        """
        url = f"{self.base_url}/yyh/llm/v0/engine"
        response = requests.get(url)
        return response.json()

    def llm_inference(self, data, user_id="tester", request_id="", cookie="", **kwargs):
        """
        执行 LLM 引擎
        """
        url = f"{self.base_url}/yyh/llm/v0/engine"
        headers = {
            "User-Id": user_id,
            "Request-Id": request_id,
            "Cookie": cookie
        }
        payload = {
            "data": data,
            **kwargs
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    def get_default_llm_engine(self):
        """
        获取默认 LLM 引擎
        """
        url = f"{self.base_url}/yyh/llm/v0/engine/default"
        response = requests.get(url)
        return response.json()

    def get_llm_engine_param(self, engine):
        """
        获取 LLM 引擎配置参数列表
        """
        url = f"{self.base_url}/yyh/llm/v0/engine/{engine}"
        response = requests.get(url)
        return response.json()

    def get_agent_engine_list(self):
        """
        获取 Agent 支持引擎列表
        """
        url = f"{self.base_url}/yyh/agent/v0/engine"
        response = requests.get(url)
        return response.json()

    def agent_inference(self, data, user_id="tester", request_id="", cookie="", conversation_id="", **kwargs):
        """
        执行 Agent 引擎
        """
        url = f"{self.base_url}/yyh/agent/v0/engine"
        headers = {
            "User-Id": user_id,
            "Request-Id": request_id,
            "Cookie": cookie
        }
        payload = {
            "data": data,
            "conversation_id": conversation_id,
            **kwargs
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    def get_default_agent_engine(self):
        """
        获取默认 Agent 引擎
        """
        url = f"{self.base_url}/yyh/agent/v0/engine/default"
        response = requests.get(url)
        return response.json()

    def get_agent_engine_param(self, engine):
        """
        获取 Agent 引擎配置参数列表
        """
        url = f"{self.base_url}/yyh/agent/v0/engine/{engine}"
        response = requests.get(url)
        return response.json()

    def create_agent_conversation(self, engine, data, user_id="tester", request_id="", cookie=""):
        """
        创建 Agent 会话
        """
        url = f"{self.base_url}/yyh/agent/v0/engine/{engine}"
        headers = {
            "User-Id": user_id,
            "Request-Id": request_id,
            "Cookie": cookie
        }
        payload = {
            "data": data
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()


# 使用示例
if __name__ == "__main__":
    logger.debug(cfg.SERVER_BASE_URL)
    client = YYAssistantAPIClient(cfg.SERVER_BASE_URL)

    # 获取 ASR 引擎列表
    #asr_engine_list = client.get_asr_engine_list()
    logger.info("ASR Engine List:", client.get_asr_engine_list())

    # 执行 ASR 推理（wav 二进制）
    # 示例数据，根据实际情况替换
    asr_data = "your-asr-data"
    asr_result = client.asr_inference_wav(asr_data)
    logger.info("ASR Inference Result:", asr_result)