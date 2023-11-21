from enums.chatgpt_enum import AiModelEnum
from handlers.chatgpt_handler import ChatGptHandler


ChatGptHandler.query_answer_and_display_streamly(
    prompt="hello",
    display_func=print,
    model_type=AiModelEnum.GPT4_1106_PREVIEW,
)