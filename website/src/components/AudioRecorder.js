import React from 'react';

function AudioRecorder({ setAudioText }) {
  const handleRecordClick = () => {
    // Just a placeholder for the audio recording functionality
    const sampleText = "Hello, this is a test of Narrato!";
    setAudioText(sampleText); // Set text from audio (we'll replace this with real functionality later)
  };

  return (
    <div>
      <button onClick={handleRecordClick}>Record Audio</button>
    </div>
  );
}

export default AudioRecorder;
