import React from 'react';

function DisplayText({ text }) {
  return (
    <div>
      <h2>Generated Text:</h2>
      <p>{text}</p>
    </div>
  );
}

export default DisplayText;
