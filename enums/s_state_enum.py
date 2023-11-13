from enum import Enum, auto


class ChatGptSStateEnum(Enum):
    CHAT_SUBMIT_BUTTON_STATE = auto()
    CHAT_MODEL_TYPE = auto()
    CHAT_HISTORY = auto()

    
class ImageGenerationSStateEnum(Enum):
    IMAGE_GENERATION_MODEL_TYPE = auto()
    IMAGE_GENERATION_SIZE_TYPE = auto()
    IMAGE_GENERATION_QUALITY_TYPE = auto()
    IMAGE_GENERATION_INPUTED_PROMPT = auto()
    IMAGE_GENERATION_GENERATED_IMAGE = auto()
    IMAGE_GENERATION_SUBMIT_BUTTON_STATE = auto()
    IMAGE_GENERATION_ERROR_MESSAGE = auto()
    