import speech_recognition as sr
from pydub import AudioSegment
import os

INPUT_PATH="./audios/"
OUTPUT_PATH="./converted/"


def converter_audio_from_whatsapp(file_path, output_ext="wav"):
    ext = os.path.splitext(file_path)[1].lower()
    file_name = os.path.split(file_path)[1]

    if ext not in [".m4a", ".ogg", ".opus"]:
        raise ValueError(f"Formato de arquivo {ext} não suportado pela aplicação.")

    if ext == ".m4a":
        audio = AudioSegment.from_file(file_path, format="m4a")
    elif ext not in [".ogg", ".opus"]:
        audio = AudioSegment.from_file(file_path, format="ogg")
    
    output_path = OUTPUT_PATH + os.path.splitext(file_name)[0] + f".{output_ext}"

    audio.export(output_path, format=output_ext)
    return


def audio_transcrption():
    recon = sr.Recognizer()

    for item in os.listdir(OUTPUT_PATH): 
        if item not in [".wav"]:
            pass

        if item == '.DS_Store':
            continue


        with sr.AudioFile(OUTPUT_PATH + item) as source:
            audio = recon.record(source)


        try:
            transcription = recon.recognize_google(audio, language='pt-BR')
            print(f"Transcrição {item}: ", transcription)
            print()

        except sr.UnknownValueError:
            print("Não consegui reconhecer o áduio")

        except sr.RequestError as e:
            print(f"Erro na requisição para a Google: ", e)
    return


def main():

    for item in os.listdir(INPUT_PATH):
        if item == '.DS_Store':
            continue

        converter_audio_from_whatsapp(file_path=INPUT_PATH + item)
    audio_transcrption()
    print("Áudios convertidos com sucesso.")


if __name__ == '__main__':
    main()
