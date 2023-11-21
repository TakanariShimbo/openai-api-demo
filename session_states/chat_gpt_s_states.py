from copy import deepcopy
from typing import List, Dict, Optional

from enums.chatgpt_enum import AiModelEnum, SenderEnum
from enums.s_state_enum import ChatGptSStateEnum
from session_states.base_s_states import BaseSState


class SubmitSState(BaseSState[bool]):
    @staticmethod
    def get_name() -> str:
        return f"{ChatGptSStateEnum.SUBMIT}"

    @staticmethod
    def get_default() -> bool:
        return False


class ErrorMessageSState(BaseSState[Optional[str]]):
    @staticmethod
    def get_name() -> str:
        return f"{ChatGptSStateEnum.ERROR_MESSAGE}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[str]:
        return None


class AiModelTypeSState(BaseSState[AiModelEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{ChatGptSStateEnum.AI_MODEL_TYPE}".replace(".", "_")

    @staticmethod
    def get_default() -> AiModelEnum:
        return AiModelEnum.NONE


class StoredHistorySState(BaseSState[List[Dict[str, str]]]):
    @staticmethod
    def get_name() -> str:
        return f"{ChatGptSStateEnum.STORED_HISTORY}".replace(".", "_")

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
            chat.pop("role_name", None)
        return chats
