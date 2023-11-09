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
        model: ImageGenerationModelEnum = ImageGenerationModelEnum.DALL_E_3,
        size: ImageGenerationSizeEnum = ImageGenerationSizeEnum.SIZE_1024X1024,
        quality: ImageGenerationQualityEnum = ImageGenerationQualityEnum.STANDARD,
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
    
    @classmethod
    def select_label(
        cls, 
        current_label: str, 
        default_label: str,
    ) -> str:
        if not current_label:
            #default label
            return default_label
        return current_label
    
    @classmethod
    def get_index(
        cls,
        input_list: list,
        input_label: str,
    ) -> int:
        return input_list.index(input_label)
    
    @classmethod
    def select_and_get_label(
        cls,
        input_list: list,
        current_label: str, 
        default_label: str,
    ) -> int:
        return cls.get_index(input_list=input_list, input_label=cls.select_label(current_label=current_label, default_label=default_label))
        
