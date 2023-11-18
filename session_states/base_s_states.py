from typing import TypeVar, Generic, Optional
import abc

import streamlit as st


T = TypeVar('T')


class BaseSState(Generic[T], abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def get_name() -> str:
        """
        This method should return the name of the session state variable.
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def get_default() -> T:
        """
        This method should return the default value for the session state variable.
        """
        pass

    @classmethod
    def get(cls) -> T:
        """
        Retrieve the value from the session state.
        Returns the default value if the key is not present.
        """
        try:
            return st.session_state[cls.get_name()]
        except:
            cls.set()
            return st.session_state[cls.get_name()]

    @classmethod
    def set(cls, value: Optional[T] = None) -> None:
        """
        Set the value in the session state.
        If no value is provided, use the default value.
        """
        if value is None:
            value = cls.get_default()
        st.session_state[cls.get_name()] = value
