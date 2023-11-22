from typing import Optional

from enums.speech_recognition_enum import LanguageEnum
from enums.s_state_enum import SpeechRecognitionSStateEnum
from s_states.base_s_states import BaseSState


class SubmitSState(BaseSState[bool]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechRecognitionSStateEnum.SUBMIT}".replace(".", "_")

    @staticmethod
    def get_default() -> bool:
        return False


class ErrorMessageSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechRecognitionSStateEnum.ERROR_MESSAGE}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None


class LanguageTypeSState(BaseSState[LanguageEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechRecognitionSStateEnum.LANGUAGE_TYPE}".replace(".", "_")

    @staticmethod
    def get_default() -> LanguageEnum:
        return LanguageEnum.JAPANESE
    

class StoredSpeechSState(BaseSState[Optional[bytes]]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechRecognitionSStateEnum.STORED_SPEECH}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[bytes]:
        return None
    

class StoredTranscriptSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechRecognitionSStateEnum.STORED_TRANSCRIPT}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None