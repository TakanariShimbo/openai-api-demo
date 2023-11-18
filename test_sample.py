from enums.chatgpt_enum import ModelEnum
from handlers.chatgpt_handler import ChatGptHandler


ChatGptHandler.query_and_display_answer_streamly(
    prompt="hello",
    display_func=print,
    model_type=ModelEnum.GPT_4_1106_PREVIEW,
)