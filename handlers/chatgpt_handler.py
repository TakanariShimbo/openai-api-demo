from typing import Any, List, Callable

from openai import OpenAI

from enums.env_enum import EnvEnum
from enums.chatgpt_enum import ModelEnum, SenderEnum


class ChatGptHandler:
    client = OpenAI(api_key=EnvEnum.DEFAULT_OPENAI_APIKEY.value)

    @classmethod
    def query(
        cls,
        prompt: str,
        chat_history: List[Any] = [],
        model_type: ModelEnum = ModelEnum.GPT_3_5_TURBO,
    ) -> str:
        copyed_chat_history = chat_history.copy()
        copyed_chat_history.append({"role": SenderEnum.USER.value, "content": prompt})

        response = cls.client.chat.completions.create(
            model=model_type.value,
            messages=copyed_chat_history
        )

        answer = response.choices[0].message.content
        return answer
    
    @classmethod
    def query_and_display_answer_streamly(
        cls,
        prompt: str,
        display_func: Callable[[str], None] = print,
        chat_history: List[Any] = [],
        model_type: ModelEnum = ModelEnum.GPT_3_5_TURBO,
    ) -> str:
        copyed_chat_history = chat_history.copy()
        copyed_chat_history.append({"role": SenderEnum.USER.value, "content": prompt})

        stream_response = cls.client.chat.completions.create(
            model=model_type.value,
            messages=copyed_chat_history,
            stream=True,
        )

        answer = ""
        for chunk in stream_response:
            answer_peace = chunk.choices[0].delta.content or "" # type: ignore
            answer += answer_peace
            display_func(answer)
        return answer