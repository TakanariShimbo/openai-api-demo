from copy import deepcopy
from typing import List, Dict

from enums.chatgpt_enum import ModelEnum, SenderEnum
from enums.s_state_enum import ChatGptSStateEnum
from session_states.base_s_states import BaseSState


class SubmitSState(BaseSState[bool]):
    @staticmethod
    def get_name() -> str:
        return f"{ChatGptSStateEnum.SUBMIT}"

    @staticmethod
    def get_default() -> bool:
        return False


class ModelSState(BaseSState[ModelEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{ChatGptSStateEnum.MODEL}"

    @staticmethod
    def get_default() -> ModelEnum:
        return ModelEnum.NONE


class ChatHistorySState(BaseSState[List[Dict[str, str]]]):
    @staticmethod
    def get_name() -> str:
        return f"{ChatGptSStateEnum.CHAT_HISTORY}"

    @staticmethod
    def get_default() -> List[Dict[str, str]]:
        return []

    @classmethod
    def add(cls, sender_type: SenderEnum, sender_name: str, content: str) -> None:
        cls.get().append(
            {
                "role": sender_type.value,
                "role_name": sender_name,
                "content": content,
            }
        )

    @classmethod
    def get_for_query(cls) -> List[Dict[str, str]]:
        chats = deepcopy(cls.get())
        for chat in chats:
            chat.pop('role_name', None)
        return chats
