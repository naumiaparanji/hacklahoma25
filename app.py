import streamlit as st
from dotenv import load_dotenv

load_dotenv()
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
from io import BytesIO

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = "You are a YouTube video summarizer. You'll be taking the transcript text and summarizing the entire video and providing the important summary in bullet formatting within 200 or 250 words. Please provide the summary of the text given here : "


def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        st.error(f"Error extracting transcript: {str(e)}")
        return None


def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text


def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp


st.title("Multiple YouTube Videos to Detailed Notes Converter")

youtube_links = st.text_area("Enter YouTube Video Links (one per line):")

if st.button("Get Detailed Notes"):
    if youtube_links:
        urls = youtube_links.split('\n')
        urls = [url.strip() for url in urls if url.strip()]

        # Create columns for side-by-side comparison
        cols = st.columns(len(urls))

        for i, (url, col) in enumerate(zip(urls, cols), 1):
            with col:
                st.markdown(f"### Video {i}")
                try:
                    video_id = url.split("=")[1]
                    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

                    transcript_text = extract_transcript_details(url)
                    if transcript_text:
                        summary = generate_gemini_content(transcript_text, prompt)
                        st.markdown("#### Detailed Notes:")
                        st.write(summary)

                        # Generate and display audio player
                        audio_fp = text_to_speech(summary)
                        st.audio(audio_fp, format='audio/mp3')

                        # Provide download button for audio
                        st.download_button(
                            label=f"Download Audio Summary",
                            data=audio_fp,
                            file_name=f"summary_audio_{i}.mp3",
                            mime="audio/mp3"
                        )
                    else:
                        st.error("Failed to extract transcript.")
                except Exception as e:
                    st.error(f"Error processing video {i}: {str(e)}")
    else:
        st.warning("Please enter at least one YouTube URL.")
