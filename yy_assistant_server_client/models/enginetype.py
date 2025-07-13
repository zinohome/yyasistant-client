from enum import Enum


class ENGINETYPE(str, Enum):
    AGENT = "AGENT"
    ASR = "ASR"
    LLM = "LLM"
    TTS = "TTS"

    def __str__(self) -> str:
        return str(self.value)
