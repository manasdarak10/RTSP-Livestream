import React from 'react';

function App() {
  return (
    <div style={{ textAlign: "center" }}>
      <h1>Live Webcam Stream</h1>
      <img
        src="http://localhost:5000/video"
        alt="Live webcam feed"
        style={{ width: "640px", height: "480px", border: "2px solid black" }}
      />
    </div>
  );
}

export default App;
