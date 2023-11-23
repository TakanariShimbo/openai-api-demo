from openai import OpenAI

from enums.env_enum import EnvEnum
from enums.chatgpt_enum import AiModelEnum
from handlers.chatgpt_handler import ChatGptHandler


ChatGptHandler.query_answer_and_display_streamly(
    client=OpenAI(api_key=EnvEnum.DEFAULT_OPENAI_APIKEY.value),
    prompt="hello",
    display_func=print,
    model_type=AiModelEnum.GPT4_1106_PREVIEW,
)