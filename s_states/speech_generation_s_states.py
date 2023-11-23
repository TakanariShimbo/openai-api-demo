from typing import Optional

from enums.speech_generation_enum import VoiceEnum
from enums.s_state_enum import SpeechGenerationSStateEnum
from s_states.base_s_states import BaseSState


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


class VoiceTypeSState(BaseSState[VoiceEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechGenerationSStateEnum.VOICE_TYPE}".replace(".", "_")

    @staticmethod
    def get_default() -> VoiceEnum:
        return VoiceEnum.ALLOY


class StoredPromptSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechGenerationSStateEnum.STORED_PROMPT}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None


class StoredSpeechSState(BaseSState[Optional[bytes]]):
    @staticmethod
    def get_name() -> str:
        return f"{SpeechGenerationSStateEnum.STORED_SPEECH}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[bytes]:
        return None
