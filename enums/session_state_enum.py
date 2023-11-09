from enum import Enum, auto


class SessionStateEnum(Enum):
    CHAT_SUBMIT_BUTTON_STATE = auto()
    CHAT_HISTORY = auto()
    CHAT_MODEL_INDEX = auto()

    IMAGE_GENERATION_MODEL_INDEX = auto()
    IMAGE_GENERATION_SIZE_INDEX = auto()
    IMAGE_GENERATION_QUALITY_INDEX = auto()
    IMAGE_GENERATION_DESCRIPTION = auto()
    IMAGE_GENERATION_URL = auto()