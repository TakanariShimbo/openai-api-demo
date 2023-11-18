from typing import Any, List, Type, TypeVar, Optional
from enum import Enum


T = TypeVar('T', bound=Enum)


class EnumHandler:
    @staticmethod
    def get_enum_members(enum: Type[T]) -> List[T]:
        return list(enum)

    @staticmethod
    def get_enum_member_names(enum: Type[T]) -> List[str]:
        return [member.name for member in enum]

    @staticmethod
    def get_enum_member_values(enum: Type[T]) -> List[Any]:
        return [member.value for member in enum]

    @staticmethod
    def name_to_enum_member(enum: Type[T], name: str) -> T:
        return enum[name]

    @staticmethod
    def value_to_enum_member(enum: Type[T], value: Any) -> T:
        for member in enum:
            if member.value == value:
                return member
        raise ValueError(f"No enum member with value {value} in {enum}")

    @staticmethod
    def enum_member_to_index(member: T) -> int:
        enum = member.__class__
        return list(enum).index(member)

    @staticmethod
    def name_to_index(enum: Type[T], name: str) -> int:
        return EnumHandler.get_enum_member_names(enum).index(name)

    @staticmethod
    def value_to_index(enum: Type[T], value: Any) -> int:
        return EnumHandler.get_enum_member_values(enum).index(value)
