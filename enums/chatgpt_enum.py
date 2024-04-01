from enum import Enum


class SenderEnum(Enum):
    USER = "user"
    ASSISTANT = "assistant"

    
class AiModelEnum(Enum):
    NONE = None
    GPT4_TURBO_PREVIEW = "gpt-4-turbo-preview"
    GPT4 = "gpt-4"
    GPT35_TURBO_1106 = "gpt-3.5-turbo-1106"
    GPT35_TURBO = "gpt-3.5-turbo"
    GPT35_TURBO_16K = "gpt-3.5-turbo-16k"

