from openai import OpenAI

from enums.image_generation_enum import AiModelEnum, SizeEnum, QualityEnum
from exceptions.exceptions import EmptyResponseException


class ImageGenerationHandler:
    @staticmethod
    def generate_image(
        client: OpenAI,
        prompt: str,
        model_type: AiModelEnum = AiModelEnum.DALLE_3,
        size_type: SizeEnum = SizeEnum.W1024xH1024,
        quality_type: QualityEnum = QualityEnum.STANDARD,
    ) -> str:
        response = client.images.generate(
            prompt=prompt,
            model=model_type.value,
            size=size_type.value,
            quality=quality_type.value,
            n=1,
        )
        image_url = response.data[0].url
        if not image_url:
            raise EmptyResponseException()
        return image_url
