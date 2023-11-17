import base64

import cv2
import numpy as np
import requests


class ImageHandler:
    @staticmethod
    def bytes_to_b64(image_bytes: bytes) -> str:
        image_b64 = base64.b64encode(s=image_bytes).decode()
        return image_b64

    @staticmethod
    def bytes_to_array_rgb(image_bytes: bytes) -> np.ndarray:
        image_bgr = cv2.imdecode(
            buf=np.frombuffer(buffer=image_bytes, dtype=np.uint8),
            flags=cv2.IMREAD_COLOR,
        )
        image_rgb = cv2.cvtColor(src=image_bgr, code=cv2.COLOR_BGR2RGB)
        return image_rgb

    @staticmethod
    def download_as_bytes(image_url: str) -> bytes:
        response = requests.get(url=image_url)
        response.raise_for_status()
        image_bytes = bytearray(response.content)
        return image_bytes

    @classmethod
    def download_as_array_rgb(cls, image_url: str) -> np.ndarray:
        image_bytes = cls.download_as_bytes(image_url=image_url)
        image_rgb = cls.bytes_to_array_rgb(image_bytes=image_bytes)
        return image_rgb
