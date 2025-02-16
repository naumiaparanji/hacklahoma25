import React, { useState } from 'react';
import AudioRecorder from './components/AudioRecorder';
import DisplayText from './components/DisplayText';
import VideoPlayer from './components/VideoPlayer';

function App() {
  const [audioText, setAudioText] = useState('');
  const [videoUrl, setVideoUrl] = useState('');

  return (
    <div className="App">
      <header className="App-header">
        <h1>Narrato</h1>
      </header>
      <main>
        {/* Audio Recording Component */}
        <AudioRecorder setAudioText={setAudioText} />
        
        {/* Displaying the transcribed text */}
        {audioText && <DisplayText text={audioText} />}
        
        {/* Video Player to display generated video */}
        {videoUrl && <VideoPlayer videoUrl={videoUrl} />}
      </main>
    </div>
  );
}

export default App;
