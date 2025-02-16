import React from 'react';
import './App.css';
import SpeechToText from './components/SpeechToText';  // Import the SpeechToText component

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Narrato</h1>
      </header>
      <main>
        <SpeechToText />  {/* Include the SpeechToText component here */}
      </main>
    </div>
  );
}

export default App;
