from typing import Union

import numpy as np
import streamlit as st

from enums.image_generation_enum import ImageGenerationSizeEnum, ImageGenerationModelEnum, ImageGenerationQualityEnum
from enums.s_state_enum import ImageGenerationSStateEnum


class ImageGenerationSStateDefaults:    
    @staticmethod
    def get_SUBMIT_BUTTON_STATE() -> bool:
        return False

    @staticmethod
    def get_MODEL_TYPE() -> ImageGenerationModelEnum:
        return ImageGenerationModelEnum.DALL_E_3

    @staticmethod
    def get_SIZE_TYPE() -> ImageGenerationSizeEnum:
        return ImageGenerationSizeEnum.SIZE_1024X1024

    @staticmethod
    def get_QUALITY_TYPE() -> ImageGenerationQualityEnum:
        return ImageGenerationQualityEnum.STANDARD
    
    @staticmethod
    def get_GENERATED_IMAGE() -> None:
        return None


class ImageGenerationSStates:
    """
    SUBMIT_BUTTON_STATE
    """

    @staticmethod
    def get_submit_button_state() -> bool:
        return st.session_state.get(
            ImageGenerationSStateEnum.IMAGE_GENERATION_SUBMIT_BUTTON_STATE.name,
            ImageGenerationSStateDefaults.get_SUBMIT_BUTTON_STATE(),
        )

    @staticmethod
    def set_submit_button_state(
        is_submitting: bool = ImageGenerationSStateDefaults.get_SUBMIT_BUTTON_STATE(),
    ) -> None:
        st.session_state[ImageGenerationSStateEnum.IMAGE_GENERATION_SUBMIT_BUTTON_STATE.name] = is_submitting

    """
    MODEL_INDEX
    """

    @staticmethod
    def get_model_type() -> ImageGenerationModelEnum:
        return st.session_state.get(
            ImageGenerationSStateEnum.IMAGE_GENERATION_MODEL_TYPE.name,
            ImageGenerationSStateDefaults.get_MODEL_TYPE(),
        )

    @staticmethod
    def set_model_type(
        model_type: ImageGenerationModelEnum = ImageGenerationSStateDefaults.get_MODEL_TYPE(),
    ) -> None:
        st.session_state[ImageGenerationSStateEnum.IMAGE_GENERATION_MODEL_TYPE.name] = model_type

    """
    SIZE_INDEX
    """

    @staticmethod
    def get_size_type() -> ImageGenerationSizeEnum:
        return st.session_state.get(
            ImageGenerationSStateEnum.IMAGE_GENERATION_SIZE_TYPE.name,
            ImageGenerationSStateDefaults.get_SIZE_TYPE(),
        )

    @staticmethod
    def set_size_type(
        size_type: ImageGenerationSizeEnum = ImageGenerationSStateDefaults.get_SIZE_TYPE(),
    ) -> None:
        st.session_state[ImageGenerationSStateEnum.IMAGE_GENERATION_SIZE_TYPE.name] = size_type

    """
    QUALITY_INDEX
    """

    @staticmethod
    def get_quality_type() -> ImageGenerationQualityEnum:
        return st.session_state.get(
            ImageGenerationSStateEnum.IMAGE_GENERATION_QUALITY_TYPE.name,
            ImageGenerationSStateDefaults.get_QUALITY_TYPE(),
        )

    @staticmethod
    def set_quality_type(
        quality_type: ImageGenerationQualityEnum = ImageGenerationSStateDefaults.get_QUALITY_TYPE(),
    ) -> None:
        st.session_state[ImageGenerationSStateEnum.IMAGE_GENERATION_QUALITY_TYPE.name] = quality_type

    """
    USER_PROMPT
    """

    @staticmethod
    def get_user_prompt() -> str:
        return st.session_state.get(ImageGenerationSStateEnum.IMAGE_GENERATION_USER_PROMPT.name, None)

    @staticmethod
    def set_user_prompt(user_prompt: str) -> None:
        st.session_state[ImageGenerationSStateEnum.IMAGE_GENERATION_USER_PROMPT.name] = user_prompt

    """
    IMAGE_URL
    """

    @staticmethod
    def get_generated_image() -> Union[np.ndarray, str, None]:
        return st.session_state.get(
            ImageGenerationSStateEnum.IMAGE_GENERATION_GENERATED_IMAGE.name, 
            ImageGenerationSStateDefaults.get_GENERATED_IMAGE(),
        )

    @staticmethod
    def set_generated_image(
        generated_image: Union[np.ndarray, str, None] = ImageGenerationSStateDefaults.get_GENERATED_IMAGE(),
    ) -> None:
        st.session_state[ImageGenerationSStateEnum.IMAGE_GENERATION_GENERATED_IMAGE.name] = generated_image
