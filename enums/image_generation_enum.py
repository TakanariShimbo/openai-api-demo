from typing import List
from enum import Enum


class ImageGenerationModelEnum(Enum):
    DALL_E_3 = "dall-e-3"
    DALL_E_2 = "dall-e-2"

    @classmethod
    def to_value_list(cls) -> List[str]:
        return [model.value for model in cls]
    
class ImageGenerationSizeEnum(Enum):
    SIZE_1024X1024 = "1024x1024"
    SIZE_1024X1792 = "1024x1792"
    SIZE_1792X1024 = "1792x1024"

    @classmethod
    def to_value_list(cls) -> List[str]:
        return [model.value for model in cls]

class ImageGenerationQualityEnum(Enum):
    STANDARD = "standard"
    HD = "hd"

    @classmethod
    def to_value_list(cls) -> List[str]:
        return [model.value for model in cls]