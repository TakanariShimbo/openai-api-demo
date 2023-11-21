from typing import Optional

from enums.speech_recognition_enum import LanguageEnum
from enums.s_state_enum import SpeechRecognitionSStateEnum
from session_states.base_s_states import BaseSState


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


class LanguageSState(BaseSState[LanguageEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechRecognitionSStateEnum.LANGUAGE}".replace(".", "_")

    @staticmethod
    def get_default() -> LanguageEnum:
        return LanguageEnum.JAPANESE
    

class SpeechSState(BaseSState[Optional[bytes]]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechRecognitionSStateEnum.SPEECH}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[bytes]:
        return None
    

class TextSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechRecognitionSStateEnum.TEXT}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None