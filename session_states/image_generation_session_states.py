from typing import List, Dict

import streamlit as st

from enums.image_generation_enum import ImageGenerationSizeEnum, ImageGenerationModelEnum, ImageGenerationQualityEnum
from enums.session_state_enum import ImageGenerationSessionStateEnum


class ImageGenerationSessionStateDefaults:
    @staticmethod
    def get_MODEL_TYPE() -> ImageGenerationModelEnum:
        return ImageGenerationModelEnum.DALL_E_3

    @staticmethod
    def get_SIZE_TYPE() -> ImageGenerationSizeEnum:
        return ImageGenerationSizeEnum.SIZE_1024X1024

    @staticmethod
    def get_QUALITY_TYPE() -> ImageGenerationQualityEnum:
        return ImageGenerationQualityEnum.STANDARD


class ImageGenerationSessionStates:
    """
    MODEL_INDEX
    """

    @staticmethod
    def get_model_type() -> ImageGenerationModelEnum:
        return st.session_state.get(
            ImageGenerationSessionStateEnum.MODEL_TYPE.name,
            ImageGenerationSessionStateDefaults.get_MODEL_TYPE(),
        )

    @staticmethod
    def set_model_type(model_type: ImageGenerationModelEnum) -> None:
        st.session_state[ImageGenerationSessionStateEnum.MODEL_TYPE.name] = model_type

    """
    SIZE_INDEX
    """

    @staticmethod
    def get_size_type() -> ImageGenerationSizeEnum:
        return st.session_state.get(
            ImageGenerationSessionStateEnum.SIZE_TYPE.name, 
            ImageGenerationSessionStateDefaults.get_SIZE_TYPE(),
        )

    @staticmethod
    def set_size_type(size_type: ImageGenerationSizeEnum) -> None:
        st.session_state[ImageGenerationSessionStateEnum.SIZE_TYPE.name] = size_type

    """
    QUALITY_INDEX
    """

    @staticmethod
    def get_quality_type() -> ImageGenerationQualityEnum:
        return st.session_state.get(
            ImageGenerationSessionStateEnum.QUALITY_TYPE.name, 
            ImageGenerationSessionStateDefaults.get_QUALITY_TYPE(),
        )

    @staticmethod
    def set_quality_type(quality_type: ImageGenerationQualityEnum) -> None:
        st.session_state[ImageGenerationSessionStateEnum.QUALITY_TYPE.name] = quality_type

    """
    USER_PROMPT
    """

    @staticmethod
    def get_user_prompt() -> str:
        return st.session_state.get(ImageGenerationSessionStateEnum.USER_PROMPT.name, None)

    @staticmethod
    def set_user_prompt(user_prompt: str) -> None:
        st.session_state[ImageGenerationSessionStateEnum.USER_PROMPT.name] = user_prompt

    """
    IMAGE_URL
    """

    @staticmethod
    def get_image_url() -> str:
        return st.session_state.get(ImageGenerationSessionStateEnum.IMAGE_URL.name, None)

    @staticmethod
    def set_image_url(image_url: str) -> None:
        st.session_state[ImageGenerationSessionStateEnum.IMAGE_URL.name] = image_url
