from enum import Enum, auto


class ChatGptSessionStateEnum(Enum):
    SUBMIT_BUTTON_STATE = auto()
    MODEL_TYPE = auto()
    CHAT_HISTORY = auto()

    
class ImageGenerationSessionStateEnum(Enum):
    MODEL_TYPE = auto()
    SIZE_TYPE = auto()
    QUALITY_TYPE = auto()
    USER_PROMPT = auto()
    IMAGE_URL = auto()
    