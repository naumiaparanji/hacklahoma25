import os
import speech_recognition as sr
from pydub import AudioSegment
from transformers import BartForConditionalGeneration, BartTokenizer
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"
import torch  # Explicitly import torch


def transcribe_audio(file_name):
    # Convert audio to WAV format
    audio = AudioSegment.from_file(file_name)
    wav_file_name = file_name.split('.')[0] + '.wav'
    audio.export(wav_file_name, format="wav")

    # Transcribe audio
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file_name) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from speech recognition service; {e}")


def abstractive_summarize(text, max_length=150):
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=40, length_penalty=2.0, num_beams=4,
                                 early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


def main():
    audio_file = "SampleAudio.wav" #E:\Hackathon2025\SampleAudio.wav"
    transcribed_text = transcribe_audio(audio_file)

    if transcribed_text:
        print("Transcription:")
        print(transcribed_text)

        summary = abstractive_summarize(transcribed_text)
        print("\nSummary:")
        print(summary)


if __name__ == "_main_":
    main()