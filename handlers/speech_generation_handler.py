from openai import OpenAI

from enums.speech_generation_enum import VoiceEnum


class SpeechGenerationHandler:
    @staticmethod
    def generate_speech(
        client: OpenAI,
        prompt: str,
        voice_type: VoiceEnum = VoiceEnum.ALLOY,
    ) -> bytes:
        response = client.audio.speech.create(
            model="tts-1",
            voice=voice_type.value,
            input=prompt,
        )
        speech_bytes = bytes()
        for data in response.iter_bytes():
            speech_bytes += data
        return speech_bytes
