import React from 'react';

function VideoPlayer({ videoUrl }) {
  return (
    <div>
      <h2>Generated Video:</h2>
      <video width="320" height="240" controls>
        <source src={videoUrl} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
}

export default VideoPlayer;
