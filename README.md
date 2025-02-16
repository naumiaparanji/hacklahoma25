# hacklahoma25

## :mantelpiece_clock: TimeTrek: A Mindful Screen Time Management App
TimeTrek is an app designed to help kids manage their screen time more effectively, promoting healthier, more mindful tech usage. The app reduces excessive screen time by summarizing YouTube videos, offering motivational messages, and incorporating a reward system with badges and leaderboards. It encourages users to reflect on the content they engage with and helps balance screen time with real-life activities.

## :zap:	Features:
**Screen Time Tracker**: Helps track and limit daily screen usage.  
**Concise YouTube Summaries**: Summarizes YouTube videos into brief, digestible content.  
**Motivational Messages**: Provides randomly selected motivational quotes to inspire users.  
**Badges and Leaderboards**: Reward system to gamify the process, making it fun for kids.  
**Daily Usage Limit**: Allows users to set a maximum daily screen time for a mindful approach to tech.  
**Reflection Prompts**: Promotes learning and self-awareness with reflective questions after summarizing videos.

## :books: Tech Stack:
**Frontend**: Streamlit  
**Backend**: Google Gemini Pro API for content generation, YouTube Transcript API  
**Text-to-Speech**: gTTS (Google Text-to-Speech) for audio summaries

## :spiral_notepad: Installation Instructions:
Clone the repository:
```
git clone https://github.com/yourusername/TimeTrek.git
```

Install the required dependencies:
```
pip install -r requirements.txt
```

Set up environment variables for the Google Gemini API.
Create a .env file and add your API key:
```
GOOGLE_API_KEY=your_api_key_here
```

Run the app:
```
streamlit run app.py
```

## :movie_camera: How it Works:
**Enter YouTube Links**: The user can input YouTube video links, and the app will extract and summarize the content.  
**Track Screen Time**: The app monitors how many videos have been summarized and notifies the user if they've exceeded their daily usage limit.  
**Rewards and Motivation**: Users are rewarded with badges for milestones like reducing screen time, and they can view the leaderboard.  
**Mindful Engagement**: The app encourages users to reflect on the summarized content and suggests real-world activities or discussions.  

## :muscle: Motivation & Goals:
TimeTrek is designed with a clear goal: to help children reduce excessive screen time, particularly on iPads, by making screen time more purposeful and engaging. The app fosters healthy tech habits while providing educational value through video summaries and reflection prompts.

## :rainbow: Future Enhancements:
Integration with more platforms to provide a broader content summary service.  
Expand the gamification elements to include more badges, achievements, and challenges.  
Advanced analytics to track overall usage trends over time.
