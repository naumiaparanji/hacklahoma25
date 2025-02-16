import React, { useState, useEffect } from 'react';

const SpeechToText = ({ onTranscript }) => {
  const [transcript, setTranscript] = useState('');
  const [isListening, setIsListening] = useState(false);

  // Check for speech recognition support
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const recognition = new SpeechRecognition();
  recognition.lang = 'en-US';
  recognition.continuous = true; // Keep listening until stopped
  recognition.interimResults = true; // Show interim results as we go

  recognition.onresult = (event) => {
    let transcriptText = '';
    for (let i = event.resultIndex; i < event.results.length; i++) {
      transcriptText += event.results[i][0].transcript;
    }
    setTranscript(transcriptText);
    onTranscript(transcriptText);  // Send the transcript to parent component
  };

  recognition.onerror = (event) => {
    console.error('Speech recognition error:', event);
  };

  recognition.onend = () => {
    setIsListening(false);
  };

  const toggleListening = () => {
    if (isListening) {
      recognition.stop();
      setIsListening(false);
    } else {
      recognition.start();
      setIsListening(true);
    }
  };

  return (
    <div style={{ textAlign: 'center', margin: '50px' }}>
      <h2>Say something...</h2>
      <button onClick={toggleListening} style={{ padding: '10px 20px', fontSize: '16px' }}>
        {isListening ? 'Stop Listening' : 'Start Listening'}
      </button>
      <div
        id="result"
        style={{
          marginTop: '20px',
          fontSize: '18px',
          border: '1px solid #ccc',
          padding: '10px',
          width: '100%',
          maxWidth: '600px',
          margin: '20px auto',
          minHeight: '50px',
        }}
      >
        {transcript}
      </div>
    </div>
  );
};

export default SpeechToText;
