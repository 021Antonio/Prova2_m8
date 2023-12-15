import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

def transcribe_audio(audio_file):
    with sr.AudioFile(audio_file) as source:
        return sr.Recognizer().recognize_google(sr.Recognizer().record(source), language="pt-BR")

def translate_text(text, target_language="en"):
    return Translator().translate(text, dest=target_language).text

def save_to_audio(text, output_file, lang="en"):
    gTTS(text=text, lang=lang).save(output_file)

# Caminho do arquivo de áudio
audio_file_path = "./audios/audio.wav"

# Transcreve o áudio para texto
transcribed_text = transcribe_audio(audio_file_path)

# Traduz o texto reconhecido para o idioma desejado (inglês por padrão)
translated_text = translate_text(transcribed_text)

# Nome do arquivo de áudio de saída (para a tradução)
output_audio_file = "./traducao/audio_traduzido.mp3"

# Salva a tradução como um arquivo de áudio
save_to_audio(translated_text, output_audio_file)
