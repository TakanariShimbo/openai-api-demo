from typing import List, Dict

import streamlit as st

from enums.session_state_enum import ImageGenerationSessionStateEnum


class ImageGenerationSessionStateDefaults:
    @staticmethod
    def get_MODEL_INDEX():
        return None

    @staticmethod
    def get_SIZE_INDEX():
        return None

    @staticmethod
    def get_CHAT_MODEL_INDEX():
        return 0


class ImageGenerationSessionStates:
    """
    MODEL_INDEX
    """

    @staticmethod
    def get_model_index() -> int:
        return st.session_state.get(
            ImageGenerationSessionStateEnum.MODEL_INDEX.name,
            ImageGenerationSessionStateDefaults.get_MODEL_INDEX(),
        )

    @staticmethod
    def set_model_index(model_label: str) -> None:
        st.session_state[ImageGenerationSessionStateEnum.MODEL_INDEX.name] = model_label

    """
    SIZE_INDEX
    """

    @staticmethod
    def get_size_index() -> int:
        return st.session_state.get(
            ImageGenerationSessionStateEnum.SIZE_INDEX.name, 
            ImageGenerationSessionStateDefaults.get_SIZE_INDEX(),
        )

    @staticmethod
    def set_size_index(size_label: str) -> None:
        st.session_state[ImageGenerationSessionStateEnum.SIZE_INDEX.name] = size_label

    """
    QUALITY_INDEX
    """

    @staticmethod
    def get_quality_index() -> int:
        return st.session_state.get(ImageGenerationSessionStateEnum.QUALITY_INDEX.name, None)

    @staticmethod
    def set_quality_index(quality_label: str) -> None:
        st.session_state[ImageGenerationSessionStateEnum.QUALITY_INDEX.name] = quality_label

    """
    USER_PROMPT
    """

    @staticmethod
    def get_user_prompt() -> int:
        return st.session_state.get(ImageGenerationSessionStateEnum.USER_PROMPT.name, None)

    @staticmethod
    def set_user_prompt(user_prompt: str) -> None:
        st.session_state[ImageGenerationSessionStateEnum.USER_PROMPT.name] = user_prompt

    """
    IMAGE_URL
    """

    @staticmethod
    def get_image_url() -> int:
        return st.session_state.get(ImageGenerationSessionStateEnum.IMAGE_URL.name, None)

    @staticmethod
    def set_image_url(image_url: str) -> None:
        st.session_state[ImageGenerationSessionStateEnum.IMAGE_URL.name] = image_url
