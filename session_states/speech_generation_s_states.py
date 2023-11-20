from typing import Optional

from enums.speech_generation_enum import VoiceEnum
from enums.s_state_enum import SpeechGenerationSStateEnum
from session_states.base_s_states import BaseSState


class SubmitSState(BaseSState[bool]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechGenerationSStateEnum.SUBMIT}".replace(".", "_")

    @staticmethod
    def get_default() -> bool:
        return False


class ErrorMessageSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechGenerationSStateEnum.ERROR_MESSAGE}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None


class PromptSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechGenerationSStateEnum.PROMPT}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None


class VoiceSState(BaseSState[VoiceEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechGenerationSStateEnum.VOICE}".replace(".", "_")

    @staticmethod
    def get_default() -> VoiceEnum:
        return VoiceEnum.ALLOY
    

class GeneratedSpeechSState(BaseSState[Optional[bytes]]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechGenerationSStateEnum.GENERATED_SPEECH}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[bytes]:
        return None
