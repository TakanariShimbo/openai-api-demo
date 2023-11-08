from enum import Enum, auto


class SessionStateType(Enum):
    CHAT_SUBMIT_BUTTON_STATE = auto()
    CHAT_HISTORY = auto()
    CHAT_MODEL_INDEX = auto()