from typing import Optional

from openai import OpenAI

from enums.env_enum import EnvEnum
from enums.global_enum import PageEnum
from enums.s_state_enum import GlobalSStateEnum
from s_states.base_s_states import BaseSState


class PageSState(BaseSState[PageEnum]):
    @staticmethod
    def get_name() -> str:
        return f"{GlobalSStateEnum.CURRENT_PAGE}".replace(".", "_")

    @staticmethod
    def get_default() -> PageEnum:
        return PageEnum.HOME


class OpenAiClientSState(BaseSState[Optional[OpenAI]]):
    @staticmethod
    def get_name() -> str:
        return f"{GlobalSStateEnum.OPENAI_CLIENT}".replace(".", "_")

    @staticmethod
    def get_default() -> Optional[OpenAI]:
        default_openai_apikey = EnvEnum.DEFAULT_OPENAI_APIKEY.value
        if not default_openai_apikey:
            return None
            
        return OpenAI(api_key=default_openai_apikey)
        