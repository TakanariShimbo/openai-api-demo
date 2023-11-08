from components.title_component import TitleComponent
from components.chat_gpt_component import ChatGptComponent


TitleComponent.set_page_configs(
    icon="💬",
    title="Chat GPT",
)

chat_gpt_component = ChatGptComponent()
chat_gpt_component.display_component()