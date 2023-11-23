from enum import Enum, auto


class GlobalSStateEnum(Enum):
    CURRENT_PAGE = auto()
    OPENAI_CLIENT = auto()


class ChatGptSStateEnum(Enum):
    SUBMIT = auto()
    ERROR_MESSAGE = auto()
    AI_MODEL_TYPE = auto()
    STORED_HISTORY = auto()


class ImageRecognitionSStateEnum(Enum):
    SUBMIT = auto()
    ERROR_MESSAGE = auto()
    STORED_PROMPT = auto()
    STORED_IMAGE = auto()
    STORED_ANSWER = auto()


class ImageGenerationSStateEnum(Enum):
    SUBMIT = auto()
    ERROR_MESSAGE = auto()
    AI_MODEL_TYPE = auto()
    SIZE_TYPE = auto()
    QUALITY_TYPE = auto()
    STORED_PROMPT = auto()
    STORED_IMAGE = auto()


class SpeechGenerationSStateEnum(Enum):
    SUBMIT = auto()
    ERROR_MESSAGE = auto()
    VOICE_TYPE = auto()
    STORED_PROMPT = auto()
    STORED_SPEECH = auto()


class SpeechRecognitionSStateEnum(Enum):
    SUBMIT = auto()
    ERROR_MESSAGE = auto()
    LANGUAGE_TYPE = auto()
    STORED_SPEECH = auto()
    STORED_TRANSCRIPT = auto()