import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from gtts import gTTS
from io import BytesIO
import time
import random
import base64
# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """Summarize the key points of this video in a concise, easy-to-digest format. 
Focus on the most important ideas and actionable insights. 
Limit the summary to 3-5 bullet points, each no longer than 20 words. 
At the end, suggest one real-world activity or discussion topic related to the video content."""

# Motivational messages
motivational_messages = [
    "Keep going! Every step forward is a step closer to achieving your goals. 🌟",
    "Great things take time. Stay focused and stay positive! 💪",
    "Believe in yourself and all that you are. You’re on the right track! 🌱",
    "Success is the sum of small efforts, repeated day in and day out. Keep at it! 🔥",
    "Every accomplishment starts with the decision to try. You’ve got this! 🌟"
]

# Function to extract transcript from YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript
    except Exception as e:
        st.error(f"Error extracting transcript: {str(e)}")
        return None

# Function to generate content summary using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Convert text to speech
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp

# Convert local image to Base64
def get_base64(file_path):
    with open(file_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    return f"data:image/jpeg;base64,{encoded}"

# Get Base64 string
img_base64 = get_base64("img.jpeg")  # Ensure "img.jpeg" is in the same directory


# CSS for the trek theme
css = f"""
    <style>
        body , [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {{
             background: url('{img_base64}') no-repeat center center fixed !important;
            background-size: cover !important;
            background-position: center;
        }}
        h2, h3, h4 {{
            color: #4b2e1c; 
        }}
        .stButton>button {{
            background-color: #656d4a;
            color: white;
            border-radius: 12px;
            padding: 10px 20px;
            box-shadow: 0px 5px 10px #656d4a;
            transition: 0.3s;
        }}
        .stTextArea textarea {{
        background: transparent !important;
        border: 2px solid #e2cfc1 !important;
        color: white !important;
        font-size: 16px !important;
    }}
    .stTextArea textarea::placeholder {{
        color: rgba(255, 255, 255, 0.6) !important;
    }}
        .stButton>button:hover {{
            background-color: #656d4a;
            color: white;
            border-color: #656d4a;
        }}
        .stTextInput>div>input {{
            background-color: #656d4a;
            border: 2px solid #e2cfc1;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .stTextInput>div>input:focus {{
            border-color: #4b2e1c;
            outline: none;
        }}
        .stMarkdown {{
            color: #3a5a40;
        }}
        h1 {{
            color: #38a3a5;
            text-align: center;
        }}
        .motivational-message {{
            text-align: center;
            font-size: 24px;
            color: #7f4f24;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        .leaderboard-badges {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }}
        .section-box {{
            padding: 5px;
            border-radius: 15px;
            background-color: rgba(255, 255, 255, 0.8);
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-bottom: 20px;
            width: 100%;
        }}
    </style>
"""

# Inject CSS
st.markdown(css, unsafe_allow_html=True)

# Sidebar layout
with st.sidebar:
    # Initialize daily_limit in session_state if it doesn't exist
    if 'daily_limit' not in st.session_state:
        st.session_state.daily_limit = 10  # Default limit

    # Set daily usage limit
    daily_limit = st.number_input("Set daily usage limit", min_value=1, max_value=20, value=st.session_state.daily_limit)
    st.session_state.daily_limit = daily_limit

    # Display a random motivational message
    st.markdown(f'<div class="motivational-message">{random.choice(motivational_messages)}</div>', unsafe_allow_html=True)

    # Display Leaderboard and Badges side by side
    st.markdown('<div class="leaderboard-badges">', unsafe_allow_html=True)
    st.markdown('<div class="section-box"><h3>Leaderboard</h3><p>1. Hermione - 100 points</p><p>2. Harry - 80 points</p><p>3. Ron - 60 points</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-box"><h3>Badges Earned</h3><p>🏆 Explorer Badge: Completed 5 videos</p><p>🎯 Focused Trekker Badge: Reduced screen time by 20% this week</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Main app logic
st.title("TimeTreak - journey to mindfulness begins here!")
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
                st.markdown(f'<div class="summary-box">', unsafe_allow_html=True)  # Wrap content in a styled div
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
                st.markdown("</div>", unsafe_allow_html=True)  # Close the styled div

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

if st.session_state.usage_count >= st.session_state.daily_limit:
    st.warning(
        f"You've reached your daily limit of {st.session_state.daily_limit} summaries. Consider revisiting tomorrow with a fresh perspective.")
    st.stop()
