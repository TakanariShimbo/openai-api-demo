from typing import List, Any
from enum import Enum


class CustomEnum(Enum):
    @classmethod
    def to_enum_list(cls) -> List[Any]:
        return [model for model in cls]
    
    @classmethod
    def to_name_list(cls) -> List[str]:
        return [model.name for model in cls]

    @classmethod
    def to_value_list(cls) -> List[Any]:
        return [model.value for model in cls]

    @classmethod
    def from_enum_to_index(cls, enum: Any) -> int:
        return cls.to_enum_list().index(enum)
    
    @classmethod
    def from_name_to_index(cls, name: str) -> int:
        return cls.to_name_list().index(name)
    
    @classmethod
    def from_value_to_index(cls, value: Any) -> int:
        return cls.to_value_list().index(value)
    
    @classmethod
    def from_name_to_enum(cls, name: str) -> Any:
        return getattr(cls, name)
    
    @classmethod
    def from_value_to_enum(cls, value: Any) -> Any:
        return cls(value)