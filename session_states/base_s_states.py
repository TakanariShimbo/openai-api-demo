from typing import TypeVar, Generic
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
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    @abc.abstractmethod
    def get_default() -> T:
        """
        This method should return the default value for the session state variable.
        """
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def get(cls) -> T:
        try:
            return st.session_state[cls.get_name()]
        except KeyError:
            cls.reset()
            return st.session_state[cls.get_name()]

    @classmethod
    def set(cls, value: T) -> None:
        st.session_state[cls.get_name()] = value

    @classmethod
    def reset(cls) -> None:
        st.session_state[cls.get_name()] = cls.get_default()