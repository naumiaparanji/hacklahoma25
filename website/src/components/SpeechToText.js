import React, { useState } from 'react';

const SpeechToText = () => {
  const [transcript, setTranscript] = useState('');
  const [isListening, setIsListening] = useState(false);

  // Check for speech recognition support
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const recognition = new SpeechRecognition();
  recognition.lang = 'en-US';
  recognition.continuous = true;
  recognition.interimResults = true;

  recognition.onresult = (event) => {
    let transcriptText = '';
    for (let i = event.resultIndex; i < event.results.length; i++) {
      transcriptText += event.results[i][0].transcript;
    }
    setTranscript(transcriptText);
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
      <h1>Speech To Text</h1>
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
