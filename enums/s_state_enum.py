from enum import Enum, auto


class GlobalSStateEnum(Enum):
    PAGE = auto()


class ChatGptSStateEnum(Enum):
    SUBMIT = auto()
    ERROR_MESSAGE = auto()
    PROMPT = auto()
    MODEL = auto()
    CHAT_HISTORY = auto()


class ImageRecognitionSStateEnum(Enum):
    SUBMIT = auto()
    ERROR_MESSAGE = auto()
    PROMPT = auto()
    UPLOADED_IMAGE = auto()
    ANSWER = auto()


class ImageGenerationSStateEnum(Enum):
    SUBMIT = auto()
    ERROR_MESSAGE = auto()
    MODEL = auto()
    SIZE = auto()
    QUALITY = auto()
    PROMPT = auto()
    GENERATED_IMAGE = auto()


class SpeechGenerationSStateEnum(Enum):
    SUBMIT = auto()
    ERROR_MESSAGE = auto()
    PROMPT = auto()
    VOICE = auto()
    GENERATED_SPEECH = auto()