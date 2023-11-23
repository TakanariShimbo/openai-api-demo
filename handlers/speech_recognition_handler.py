from typing import Any

from openai import OpenAI

from enums.speech_recognition_enum import LanguageEnum


class SpeechRecognitionHandler:
    @staticmethod
    def recognize_speech(
        client: OpenAI,
        speech_file: Any,
        language_type: LanguageEnum = LanguageEnum.JAPANESE,
    ) -> str:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            language=language_type.value,
            file=speech_file,
        )
        return transcript.text
