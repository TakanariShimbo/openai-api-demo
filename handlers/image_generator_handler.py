from typing import Any, Dict, List, Callable

from openai import OpenAI

from enums.sender_enum import SenderEnum
from enums.image_generator_enum import (
    ImageGeneratorModelEnum,
    ImageGeneratorSizeEnum,
    ImageGeneratorQualityEnum,
)
from enums.env_enum import EnvEnum


class ImageGeneratorHandler:
    client = OpenAI(api_key=EnvEnum.OPENAI_APIKEY.value)

    @classmethod
    def get_image_url(
        cls,
        prompt: str,
        model: ImageGeneratorModelEnum = ImageGeneratorModelEnum.DALL_E_3,
        size: ImageGeneratorSizeEnum = ImageGeneratorSizeEnum.SIZE_1024X1024,
        quality: ImageGeneratorQualityEnum = ImageGeneratorQualityEnum.STANDARD,
    ) -> str:
        response = cls.client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality=quality,
            n=1,
        )
        image_url = response.data[0].url
        return image_url
