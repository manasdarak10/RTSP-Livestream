import React from "react";

function App() {
  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>📡 Live RTSP Stream</h1>

      <div style={{ marginTop: "20px" }}>
        <img
          src="http://localhost:5000/video_feed"
          alt="Live Stream"
          width="800"
          style={{ border: "2px solid #333" }}
        />
      </div>
    </div>
  );
}

export default App;
