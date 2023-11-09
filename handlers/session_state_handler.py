from typing import List, Dict

import streamlit as st

from enums.sender_enum import SenderEnum
from enums.session_state_enum import SessionStateEnum


class SessionStateHandler:
    """
    CHAT_SUBMIT_BUTTON_STATE
    """
    @staticmethod
    def get_chat_submit_button_state() -> bool:
        return st.session_state.get(SessionStateEnum.CHAT_SUBMIT_BUTTON_STATE.name, False)

    @staticmethod
    def set_chat_submit_button_state(is_submitting: bool = False) -> None:
        st.session_state[SessionStateEnum.CHAT_SUBMIT_BUTTON_STATE.name] = is_submitting

    """
    CHAT_HISTORY
    """
    @staticmethod
    def get_chat_history() -> List[Dict[str, str]]:
        return st.session_state.get(SessionStateEnum.CHAT_HISTORY.name, [])

    @staticmethod
    def add_chat_history(sender_type: SenderEnum, content: str) -> None:
        chat_dict = {"role": sender_type.value, "content": content}
        try:
            st.session_state[SessionStateEnum.CHAT_HISTORY.name].append(chat_dict)
        except (AttributeError, KeyError):
            st.session_state[SessionStateEnum.CHAT_HISTORY.name] = [chat_dict]

    @staticmethod
    def reset_chat_history() -> None:
        st.session_state[SessionStateEnum.CHAT_HISTORY.name] = []

    """
    CHAT_MODEL_INDEX
    """
    @staticmethod
    def get_chat_model_index() -> int:
        return st.session_state.get(SessionStateEnum.CHAT_MODEL_INDEX.name, 0)

    @staticmethod
    def set_chat_model_index(model_index: int = 0) -> None:
        st.session_state[SessionStateEnum.CHAT_MODEL_INDEX.name] = model_index

    """
    IMAGE_GENERATOR_MODEL_INDEX
    """
    @staticmethod
    def get_image_generation_model_label() -> int:
        return st.session_state.get(SessionStateEnum.IMAGE_GENERATION_MODEL_INDEX.name, None)

    @staticmethod
    def set_image_generation_model_label(model_label: str) -> None:
        st.session_state[SessionStateEnum.IMAGE_GENERATION_MODEL_INDEX.name] = model_label
    
    """
    IMAGE_GENERATOR_SIZE_INDEX
    """
    @staticmethod
    def get_image_generation_size_label() -> int:
        return st.session_state.get(SessionStateEnum.IMAGE_GENERATION_SIZE_INDEX.name, None)

    @staticmethod
    def set_image_generation_size_label(size_label: str) -> None:
        st.session_state[SessionStateEnum.IMAGE_GENERATION_SIZE_INDEX.name] = size_label

    """
    IMAGE_GENERATOR_QUALITY_INDEX
    """
    @staticmethod
    def get_image_generation_quality_label() -> int:
        return st.session_state.get(SessionStateEnum.IMAGE_GENERATION_QUALITY_INDEX.name, None)

    @staticmethod
    def set_image_generation_quality_label(quality_label: str) -> None:
        st.session_state[SessionStateEnum.IMAGE_GENERATION_QUALITY_INDEX.name] = quality_label

    """
    IMAGE_GENERATOR_DESCRIPTION
    """
    @staticmethod
    def get_image_generation_description() -> int:
        return st.session_state.get(SessionStateEnum.IMAGE_GENERATION_DESCRIPTION.name, None)

    @staticmethod
    def set_image_generation_description(description: str) -> None:
        st.session_state[SessionStateEnum.IMAGE_GENERATION_DESCRIPTION.name] = description

    """
    IMAGE_GENERATOR_IMAGE_URL
    """
    @staticmethod
    def get_image_generation_image_url() -> int:
        return st.session_state.get(SessionStateEnum.IMAGE_GENERATION_URL.name, None)

    @staticmethod
    def set_image_generation_image_url(image_url: str) -> None:
        st.session_state[SessionStateEnum.IMAGE_GENERATION_URL.name] = image_url

