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


class AiModelTypeSState(BaseSState[AiModelEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.AI_MODEL_TYPE}".replace(".", "_")

    @staticmethod
    def get_default() -> AiModelEnum:
        return AiModelEnum.DALLE_3


class SizeTypeSState(BaseSState[SizeEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.SIZE_TYPE}".replace(".", "_")

    @staticmethod
    def get_default() -> SizeEnum:
        return SizeEnum.W1024xH1024


class QualityTypeSState(BaseSState[QualityEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.QUALITY_TYPE}".replace(".", "_")

    @staticmethod
    def get_default() -> QualityEnum:
        return QualityEnum.STANDARD


class StoredPromptSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.STORED_PROMPT}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None


class StoredImageSState(BaseSState[Union[np.ndarray, str]]):
    @staticmethod
    def get_name() -> str:
        return f"{ImageGenerationSStateEnum.STORED_IMAGE}".replace(".", "_")

    @staticmethod
    def get_default() -> Union[np.ndarray, str]:
        return DUMMY_IMAGE
