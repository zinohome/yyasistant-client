from enum import Enum


class PARAMTYPE(str, Enum):
    BOOL = "bool"
    FLOAT = "float"
    INT = "int"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
