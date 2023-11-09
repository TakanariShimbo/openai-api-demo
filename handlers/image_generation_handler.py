from typing import Any, Dict, List, Callable

from openai import OpenAI

from enums.sender_enum import SenderEnum
from enums.image_generation_enum import (
    ImageGenerationModelEnum,
    ImageGenerationSizeEnum,
    ImageGenerationQualityEnum,
)
from enums.env_enum import EnvEnum


class ImageGenerationHandler:
    client = OpenAI(api_key=EnvEnum.OPENAI_APIKEY.value)

    @classmethod
    def get_image_url(
        cls,
        prompt: str,
        model_type: ImageGenerationModelEnum = ImageGenerationModelEnum.DALL_E_3,
        size_type: ImageGenerationSizeEnum = ImageGenerationSizeEnum.SIZE_1024X1024,
        quality_type: ImageGenerationQualityEnum = ImageGenerationQualityEnum.STANDARD,
    ) -> str:
        response = cls.client.images.generate(
            prompt=prompt,
            model=model_type.value,
            size=size_type.value,
            quality=quality_type.value,
            n=1,
        )
        image_url = response.data[0].url
        return image_url
