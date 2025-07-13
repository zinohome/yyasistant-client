from enum import Enum


class INFERTYPE(str, Enum):
    NORMAL = "normal"
    STREAM = "stream"

    def __str__(self) -> str:
        return str(self.value)
