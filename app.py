import streamlit as st
from dotenv import load_dotenv

load_dotenv()
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
from io import BytesIO
import time

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """Summarize the key points of this video in a concise, easy-to-digest format. 
Focus on the most important ideas and actionable insights. 
Limit the summary to 3-5 bullet points, each no longer than 20 words. 
At the end, suggest one real-world activity or discussion topic related to the video content."""


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


st.title("Mindful YouTube Summary Assistant")

st.markdown("""
This tool helps you extract key insights from YouTube videos without spending excessive time watching them. 
It respects your attention by providing concise summaries and encouraging real-world engagement.
""")

youtube_links = st.text_area("Enter YouTube Video Links (one per line):")

if st.button("Get Mindful Summaries"):
    if youtube_links:
        urls = [url.strip() for url in youtube_links.split('\n') if url.strip()]

        with st.spinner("Processing videos... Please take a moment to breathe and reflect."):
            time.sleep(3)  # Encourage a brief pause for mindfulness

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
                        st.markdown("#### Key Insights:")
                        st.write(summary)

                        audio_fp = text_to_speech(summary)
                        with st.expander("Listen to Summary"):
                            st.audio(audio_fp, format='audio/mp3')

                        st.download_button(
                            label="Download Audio Summary",
                            data=audio_fp,
                            file_name=f"mindful_summary_{i}.mp3",
                            mime="audio/mp3"
                        )
                    else:
                        st.error("Failed to extract transcript.")
                except Exception as e:
                    st.error(f"Error processing video {i}: {str(e)}")

        st.markdown("""
        ## Mindful Reflection
        Now that you've reviewed the summaries, consider:
        - Which insight resonated with you the most?
        - How can you apply one of these ideas in your daily life?
        - Is there someone you'd like to discuss these topics with?

        Remember, the goal is to learn efficiently and apply knowledge meaningfully, not to consume endless content.
        """)

    else:
        st.warning("Please enter at least one YouTube URL.")

# Add a mindful usage tracker
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

st.session_state.usage_count += 1

if st.session_state.usage_count % 5 == 0:
    st.markdown("""
    ### Mindful Technology Use Reminder
    You've used this tool several times today. Consider taking a break to reflect on what you've learned 
    or engage in a non-digital activity related to the content you've summarized.
    """)

# Add a daily limit feature
if 'daily_limit' not in st.session_state:
    st.session_state.daily_limit = 10

daily_limit = st.sidebar.number_input("Set daily usage limit", min_value=1, max_value=20,
                                      value=st.session_state.daily_limit)
st.session_state.daily_limit = daily_limit

if st.session_state.usage_count >= st.session_state.daily_limit:
    st.warning(
        f"You've reached your daily limit of {st.session_state.daily_limit} summaries. Consider revisiting tomorrow with a fresh perspective.")
    st.stop()
