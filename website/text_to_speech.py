import speech_recognition as sr
import os

r = sr.Recognizer()  # Instantiate the Recognizer class

with sr.Microphone() as source:  # Use parentheses to call the Microphone class
    print("Listening...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("Transcription: ", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
except Exception as e:
    print("An error occurred: {0}".format(e))