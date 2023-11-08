import streamlit as st


class TitleComponent:
    @staticmethod
    def set_page_configs(icon: str, title: str) -> None:
        st.set_page_config(
            page_title=title,
            page_icon=icon,
        )
        st.write(f"## {icon}{title}")
        st.sidebar.header(title)