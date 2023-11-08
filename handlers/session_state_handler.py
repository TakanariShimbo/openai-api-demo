from typing import List, Dict

import streamlit as st

from enums.sender_enum import SenderEnum
from enums.session_state_enum import SessionStateType


class SessionStateHandler:
    """
    CHAT_SUBMIT_BUTTON_STATE
    """
    @staticmethod
    def get_chat_submit_button_state() -> bool:
        return st.session_state.get(SessionStateType.CHAT_SUBMIT_BUTTON_STATE.name, False)

    @staticmethod
    def set_chat_submit_button_state(is_submitting: bool = False) -> None:
        setattr(st.session_state, SessionStateType.CHAT_SUBMIT_BUTTON_STATE.name, is_submitting)

    """
    CHAT_HISTORY
    """
    @staticmethod
    def get_chat_history() -> List[Dict[str, str]]:
        return st.session_state.get(SessionStateType.CHAT_HISTORY.name, [])

    @staticmethod
    def add_chat_history(sender_type: SenderEnum, content: str) -> None:
        chat_dict = {"role": sender_type.value, "content": content}
        try:
            st.session_state[SessionStateType.CHAT_HISTORY.name].append(chat_dict)
        except (AttributeError, KeyError):
            setattr(st.session_state, SessionStateType.CHAT_HISTORY.name, [chat_dict])

    @staticmethod
    def reset_chat_history() -> None:
        setattr(st.session_state, SessionStateType.CHAT_HISTORY.name, [])

    """
    CHAT_MODEL_INDEX
    """
    @staticmethod
    def get_chat_model_index() -> int:
        return st.session_state.get(SessionStateType.CHAT_MODEL_INDEX.name, 0)

    @staticmethod
    def set_chat_model_index(model_index: int = 0) -> None:
        setattr(st.session_state, SessionStateType.CHAT_MODEL_INDEX.name, model_index)
