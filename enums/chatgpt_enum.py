from enum import Enum


class SenderEnum(Enum):
    USER = "user"
    ASSISTANT = "assistant"

    
class AiModelEnum(Enum):
    NONE = None
    GPT4O = "gpt-4o"
    GPT4_TURBO = "gpt-4-turbo"
    GPT4 = "gpt-4"
    GPT35_TURBO = "gpt-3.5-turbo"
    GPT35_TURBO_16K = "gpt-3.5-turbo-16k"

