from enum import Enum


class AiModelEnum(Enum):
    DALLE_3 = "dall-e-3"
    DALLE_2 = "dall-e-2"


class SizeEnum(Enum):
    W1024xH1024 = "1024x1024"
    W1024xH1792 = "1024x1792"
    W1792xH1024 = "1792x1024"


class QualityEnum(Enum):
    STANDARD = "standard"
    HD = "hd"
