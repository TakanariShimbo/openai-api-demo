from typing import List
from enum import Enum


class ChatGptEnum(Enum):
    GPT_4_1106_PREVIEW = "gpt-4-1106-preview"
    GPT_4 = "gpt-4"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"

    @classmethod
    def to_enum_list(cls) -> List["ChatGptEnum"]:
        return [model for model in cls]
    
    @classmethod
    def to_name_list(cls) -> List[str]:
        return [model.name for model in cls]

    @classmethod
    def to_value_list(cls) -> List[str]:
        return [model.value for model in cls]

    @classmethod
    def from_enum_to_index(cls, enum: "ChatGptEnum") -> int:
        return cls.to_enum_list().index(enum)
    
    @classmethod
    def from_name_to_index(cls, name: str) -> int:
        return cls.to_name_list().index(name)
    
    @classmethod
    def from_value_to_index(cls, value: str) -> int:
        return cls.to_value_list().index(value)
    
    @classmethod
    def from_name_to_enum(cls, name: str) -> "ChatGptEnum":
        return getattr(cls, name)
    
    @classmethod
    def from_value_to_enum(cls, value: str) -> "ChatGptEnum":
        return cls(value)