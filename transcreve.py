import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def transcreve_audio(caminho_audio, language='pt', response_format='text'):
    with open(caminho_audio, 'rb') as arquivo_audio:
        transcricao = openai.audio.transcriptions.create(
            model='whisper-1',
            language=language,
            response_format=response_format,
            file=arquivo_audio,
        )
    return transcricao

transcreve_audio('audio.mp3', response_format='srt')