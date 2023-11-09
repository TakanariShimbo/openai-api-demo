from enums.custom_enum import CustomEnum


class ImageGenerationModelEnum(CustomEnum):
    DALL_E_3 = "dall-e-3"
    DALL_E_2 = "dall-e-2"


class ImageGenerationSizeEnum(CustomEnum):
    SIZE_1024X1024 = "1024x1024"
    SIZE_1024X1792 = "1024x1792"
    SIZE_1792X1024 = "1792x1024"


class ImageGenerationQualityEnum(CustomEnum):
    STANDARD = "standard"
    HD = "hd"
