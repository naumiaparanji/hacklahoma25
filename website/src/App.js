import React, { useState } from 'react';
import SpeechToText from './components/SpeechToText';
import VideoPlayer from './components/VideoPlayer';

const App = () => {
  const [videoUrl, setVideoUrl] = useState('');

  const handleTranscript = (transcript) => {
    // Match the transcript and select the corresponding video
    if (transcript.toLowerCase().includes("spiderman is surfing")) {
      setVideoUrl('./images/spiderman-surfing.mp4'); // Hardcoded video URL for "Spiderman is Surfing"
    } else if (transcript.toLowerCase().includes("girl walks home")) {
      setVideoUrl('/path/to/girl-walks-home.mp4'); // Hardcoded video URL for "Girl Walks Home"
    } else {
      setVideoUrl(''); // Clear video if transcript doesn't match
    }
  };

  return (
    <div>
      <h1>Speech to Video Example</h1>
      <SpeechToText onTranscript={handleTranscript} />
      {videoUrl && <VideoPlayer videoUrl={videoUrl} />}
    </div>
  );
};

export default App;
