from typing import Optional

import numpy as np

from enums.s_state_enum import ImageRecognitionSStateEnum
from session_states.base_s_states import BaseSState


class SubmitSState(BaseSState[bool]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageRecognitionSStateEnum.SUBMIT}".replace(".", "_")

    @staticmethod
    def get_default() -> bool:
        return False


class ErrorMessageSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageRecognitionSStateEnum.ERROR_MESSAGE}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None


class StoredPromptSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageRecognitionSStateEnum.STORED_PROMPT}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None


class StoredImageSState(BaseSState[Optional[np.ndarray]]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageRecognitionSStateEnum.STORED_IMAGE}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[np.ndarray]:
        return None
    

class StoredAnswerSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageRecognitionSStateEnum.STORED_ANSWER}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None
