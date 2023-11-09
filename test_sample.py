from enums.chatgpt_enum import ChatGptModelEnum
from handlers.chatgpt_handler import ChatGptHandler


ChatGptHandler.query_and_display_answer_streamly(
    prompt="hello",
    display_func=print,
    model_type=ChatGptModelEnum.GPT_4_1106_PREVIEW,
)