from typing import Any, List
from enum import Enum


class ImageGenerationModelEnum(Enum):
    DALL_E_3 = "dall-e-3"
    DALL_E_2 = "dall-e-2"

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


class ImageGenerationSizeEnum(Enum):
    SIZE_1024X1024 = "1024x1024"
    SIZE_1024X1792 = "1024x1792"
    SIZE_1792X1024 = "1792x1024"

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


class ImageGenerationQualityEnum(Enum):
    STANDARD = "standard"
    HD = "hd"

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
