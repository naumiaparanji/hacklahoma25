import speech_recognition as sr
from transformers import BartForConditionalGeneration, BartTokenizer
import time


def listen_and_transcribe(timeout=10):
    r = sr.Recognizer()
    r.pause_threshold = timeout  # Set pause threshold to 10 seconds

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=timeout)
            text = r.recognize_google(audio)
            print(f"Transcription: {text}")
            return text
        except sr.WaitTimeoutError:
            print("No speech detected for 10 seconds. Stopping.")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

def abstractive_summarize(text, max_length=1500):
    # Load pre-trained model and tokenizer
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

    # Tokenize the input text
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs, max_length=max_length, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary
if __name__ == "_main_":
    transcribed_text = listen_and_transcribe()
    transcribed_text_to_summarize = transcribed_text
    summary = abstractive_summarize(transcribed_text_to_summarize)
    print(summary)