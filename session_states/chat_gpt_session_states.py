from typing import List, Dict

import streamlit as st

from enums.sender_enum import SenderEnum
from enums.chatgpt_enum import ChatGptModelEnum
from enums.session_state_enum import ChatGptSessionStateEnum


class ChatGptSessionStateDefaults:
    @staticmethod
    def get_SUBMIT_BUTTON_STATE() -> bool:
        return False

    @staticmethod
    def get_CHAT_HISTORY() -> List[Dict[str, str]]:
        return []

    @staticmethod
    def get_MODEL_TYPE() -> ChatGptModelEnum:
        return ChatGptModelEnum.GPT_4_1106_PREVIEW


class ChatGptSessionStates:
    """
    SUBMIT_BUTTON_STATE
    """

    @staticmethod
    def get_submit_button_state() -> bool:
        return st.session_state.get(
            ChatGptSessionStateEnum.SUBMIT_BUTTON_STATE.name,
            ChatGptSessionStateDefaults.get_SUBMIT_BUTTON_STATE(),
        )

    @staticmethod
    def set_submit_button_state(
        is_submitting: bool = ChatGptSessionStateDefaults.get_SUBMIT_BUTTON_STATE(),
    ) -> None:
        st.session_state[ChatGptSessionStateEnum.SUBMIT_BUTTON_STATE.name] = is_submitting

    """
    CHAT_HISTORY
    """

    @staticmethod
    def get_chat_history() -> List[Dict[str, str]]:
        return st.session_state.get(
            ChatGptSessionStateEnum.CHAT_HISTORY.name,
            ChatGptSessionStateDefaults.get_CHAT_HISTORY(),
        )

    @staticmethod
    def add_chat_history(sender_type: SenderEnum, content: str) -> None:
        chat_dict = {"role": sender_type.value, "content": content}
        try:
            st.session_state[ChatGptSessionStateEnum.CHAT_HISTORY.name].append(chat_dict)
        except (AttributeError, KeyError):
            st.session_state[ChatGptSessionStateEnum.CHAT_HISTORY.name] = [chat_dict]

    @staticmethod
    def reset_chat_history() -> None:
        st.session_state[ChatGptSessionStateEnum.CHAT_HISTORY.name] = ChatGptSessionStateDefaults.get_CHAT_HISTORY()

    """
    MODEL_INDEX
    """

    @staticmethod
    def get_model_type() -> ChatGptModelEnum:
        return st.session_state.get(
            ChatGptSessionStateEnum.MODEL_TYPE.name,
            ChatGptSessionStateDefaults.get_MODEL_TYPE(),
        )

    @staticmethod
    def set_model_type(
        model_type: ChatGptModelEnum = ChatGptSessionStateDefaults.get_MODEL_TYPE(),
    ) -> None:
        st.session_state[ChatGptSessionStateEnum.MODEL_TYPE.name] = model_type
