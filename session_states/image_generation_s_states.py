from typing import Union, Optional

import cv2
import numpy as np

from enums.image_generation_enum import SizeEnum, AiModelEnum, QualityEnum
from enums.s_state_enum import ImageGenerationSStateEnum
from session_states.base_s_states import BaseSState


DUMMY_IMAGE = cv2.imread(filename="images/dummy.jpg", flags=cv2.IMREAD_COLOR)


class SubmitSState(BaseSState[bool]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.SUBMIT}".replace(".", "_")

    @staticmethod
    def get_default() -> bool:
        return False


class ErrorMessageSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.ERROR_MESSAGE}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None


class AiModelSState(BaseSState[AiModelEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.MODEL}".replace(".", "_")

    @staticmethod
    def get_default() -> AiModelEnum:
        return AiModelEnum.DALL_E_3


class SizeSState(BaseSState[SizeEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.SIZE}".replace(".", "_")

    @staticmethod
    def get_default() -> SizeEnum:
        return SizeEnum.SIZE_1024X1024


class QualitySState(BaseSState[QualityEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.QUALITY}".replace(".", "_")

    @staticmethod
    def get_default() -> QualityEnum:
        return QualityEnum.STANDARD


class PromptSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.PROMPT}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None


class GeneratedImageSState(BaseSState[Union[np.ndarray, str]]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.GENERATED_IMAGE}".replace(".", "_")

    @staticmethod
    def get_default() -> Union[np.ndarray, str]:
        return DUMMY_IMAGE
