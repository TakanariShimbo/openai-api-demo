import cv2
import numpy as np
from openai import OpenAI

from enums.image_generation_enum import (
    ImageGenerationModelEnum,
    ImageGenerationSizeEnum,
    ImageGenerationQualityEnum,
)
from enums.env_enum import EnvEnum


class ImageGenerationHandler:
    client = OpenAI(api_key=EnvEnum.DEFAULT_OPENAI_APIKEY.value)
    DUMMY_IMAGE = cv2.imread(filename="images/dummy.jpg", flags=cv2.IMREAD_COLOR)

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

    @classmethod
    def get_DUMMY_IMAGE(cls) -> np.ndarray:
        return cls.DUMMY_IMAGE
