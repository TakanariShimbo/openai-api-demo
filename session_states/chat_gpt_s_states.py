from typing import List, Dict

import streamlit as st

from enums.chatgpt_enum import ChatGptModelEnum, ChatSenderEnum
from enums.s_state_enum import ChatGptSStateEnum


class ChatGptSStateDefaults:
    @staticmethod
    def get_SUBMIT_BUTTON_STATE() -> bool:
        return False

    @staticmethod
    def get_MODEL_TYPE() -> ChatGptModelEnum:
        return ChatGptModelEnum.GPT_4_1106_PREVIEW

    @staticmethod
    def get_CHAT_HISTORY() -> List[Dict[str, str]]:
        return []


class ChatGptSStates:
    """
    SUBMIT_BUTTON_STATE
    """

    @staticmethod
    def get_submit_button_state() -> bool:
        return st.session_state.get(
            ChatGptSStateEnum.CHAT_SUBMIT_BUTTON_STATE.name,
            ChatGptSStateDefaults.get_SUBMIT_BUTTON_STATE(),
        )

    @staticmethod
    def set_submit_button_state(
        is_submitting: bool = ChatGptSStateDefaults.get_SUBMIT_BUTTON_STATE(),
    ) -> None:
        st.session_state[ChatGptSStateEnum.CHAT_SUBMIT_BUTTON_STATE.name] = is_submitting

    """
    MODEL_TYPE
    """

    @staticmethod
    def get_model_type() -> ChatGptModelEnum:
        return st.session_state.get(
            ChatGptSStateEnum.CHAT_MODEL_TYPE.name,
            ChatGptSStateDefaults.get_MODEL_TYPE(),
        )

    @staticmethod
    def set_model_type(
        model_type: ChatGptModelEnum = ChatGptSStateDefaults.get_MODEL_TYPE(),
    ) -> None:
        st.session_state[ChatGptSStateEnum.CHAT_MODEL_TYPE.name] = model_type

    """
    CHAT_HISTORY
    """

    @staticmethod
    def get_chat_history() -> List[Dict[str, str]]:
        return st.session_state.get(
            ChatGptSStateEnum.CHAT_HISTORY.name,
            ChatGptSStateDefaults.get_CHAT_HISTORY(),
        )

    @staticmethod
    def add_chat_history(sender_type: ChatSenderEnum, content: str) -> None:
        chat_dict = {"role": sender_type.value, "content": content}
        try:
            st.session_state[ChatGptSStateEnum.CHAT_HISTORY.name].append(chat_dict)
        except (AttributeError, KeyError):
            st.session_state[ChatGptSStateEnum.CHAT_HISTORY.name] = [chat_dict]

    @staticmethod
    def reset_chat_history() -> None:
        st.session_state[ChatGptSStateEnum.CHAT_HISTORY.name] = ChatGptSStateDefaults.get_CHAT_HISTORY()
