from openai import OpenAI

from enums.image_generation_enum import (
    ModelEnum,
    SizeEnum,
    QualityEnum,
)
from enums.env_enum import EnvEnum


class ImageGenerationHandler:
    client = OpenAI(api_key=EnvEnum.DEFAULT_OPENAI_APIKEY.value)

    @classmethod
    def get_image_url(
        cls,
        prompt: str,
        model_type: ModelEnum = ModelEnum.DALL_E_3,
        size_type: SizeEnum = SizeEnum.SIZE_1024X1024,
        quality_type: QualityEnum = QualityEnum.STANDARD,
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
