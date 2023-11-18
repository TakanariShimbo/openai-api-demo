from openai import OpenAI

from enums.speech_generation_enum import SpeechGenerationVoiceEnum
from enums.env_enum import EnvEnum


class SpeechGenerationHandler:
    client = OpenAI(api_key=EnvEnum.DEFAULT_OPENAI_APIKEY.value)

    @classmethod
    def get_speech_bytes(
        cls,
        prompt: str,
        voice: SpeechGenerationVoiceEnum = SpeechGenerationVoiceEnum.ALLOY,
    ) -> bytes:
        response = cls.client.audio.speech.create(
            model="tts-1",
            voice=voice.value,
            input=prompt
        )
        speech_bytes = bytes()
        for data in response.iter_bytes():
            speech_bytes += data
        return speech_bytes
