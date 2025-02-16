from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play


def text_to_speech(text, language='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the audio to a BytesIO object
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    # Load the audio using pydub
    audio = AudioSegment.from_mp3(fp)

    # Play the audio
    play(audio)


# Example usage
text = "Hello, this is a text-to-speech conversion using Python, gTTS, and pydub."
text_to_speech(text)
