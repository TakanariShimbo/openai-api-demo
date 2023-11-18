from enum import Enum, auto


class ChatGptSStateEnum(Enum):
    SUBMIT = auto()
    MODEL = auto()
    CHAT_HISTORY = auto()

    
class ImageGenerationSStateEnum(Enum):
    SUBMIT = auto()
    ERROR_MESSAGE = auto()
    MODEL = auto()
    SIZE = auto()
    QUALITY = auto()
    PROMPT = auto()
    GENERATED_IMAGE = auto()
    