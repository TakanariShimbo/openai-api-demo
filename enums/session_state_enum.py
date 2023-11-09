from enum import Enum, auto


class ChatGptSessionStateEnum(Enum):
    CHAT_SUBMIT_BUTTON_STATE = auto()
    CHAT_MODEL_TYPE = auto()
    CHAT_HISTORY = auto()

    
class ImageGenerationSessionStateEnum(Enum):
    IMAGE_GENERATION_MODEL_TYPE = auto()
    IMAGE_GENERATION_SIZE_TYPE = auto()
    IMAGE_GENERATION_QUALITY_TYPE = auto()
    IMAGE_GENERATION_USER_PROMPT = auto()
    IMAGE_GENERATION_IMAGE_URL = auto()
    