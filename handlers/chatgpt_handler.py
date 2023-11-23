from typing import Any, List, Callable

from openai import OpenAI

from enums.chatgpt_enum import AiModelEnum, SenderEnum
from exceptions.exceptions import InvalidModelTypeException, EmptyResponseException


class ChatGptHandler:
    @staticmethod
    def query_answer(
        client: OpenAI,
        prompt: str,
        chat_history: List[Any] = [],
        model_type: AiModelEnum = AiModelEnum.GPT35_TURBO,
    ) -> str:
        if model_type == AiModelEnum.NONE:
            raise InvalidModelTypeException()

        copyed_chat_history = chat_history.copy()
        copyed_chat_history.append({"role": SenderEnum.USER.value, "content": prompt})

        response = client.chat.completions.create(model=model_type.value, messages=copyed_chat_history)

        answer = response.choices[0].message.content
        if not answer:
            raise EmptyResponseException()
        return answer

    @staticmethod
    def query_answer_and_display_streamly(
        client: OpenAI,
        prompt: str,
        display_func: Callable[[str], None] = print,
        chat_history: List[Any] = [],
        model_type: AiModelEnum = AiModelEnum.GPT35_TURBO,
    ) -> str:
        if model_type == AiModelEnum.NONE:
            raise InvalidModelTypeException()

        copyed_chat_history = chat_history.copy()
        copyed_chat_history.append({"role": SenderEnum.USER.value, "content": prompt})

        stream_response = client.chat.completions.create(
            model=model_type.value,
            messages=copyed_chat_history,
            stream=True,
        )

        answer = ""
        for chunk in stream_response:
            answer_peace = chunk.choices[0].delta.content or ""  # type: ignore
            answer += answer_peace
            display_func(answer)
        return answer
