from enum import Enum


class ChatSenderEnum(Enum):
    USER = "user"
    ASSISTANT = "assistant"

    
class ChatGptModelEnum(Enum):
    GPT_4_1106_PREVIEW = "gpt-4-1106-preview"
    GPT_4 = "gpt-4"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"

