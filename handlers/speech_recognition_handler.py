from typing import Any

from openai import OpenAI

from enums.env_enum import EnvEnum
from enums.speech_recognition_enum import LanguageEnum


class SpeechRecognitionHandler:
    client = OpenAI(api_key=EnvEnum.DEFAULT_OPENAI_APIKEY.value)

    @classmethod
    def recognize_speech(
        cls,
        speech_file: Any,
        language_type: LanguageEnum = LanguageEnum.JAPANESE,
    ) -> str:
        transcript = cls.client.audio.transcriptions.create(
            model="whisper-1", 
            language=language_type.value,
            file=speech_file,
        )
        return transcript.text
