import React, { useState } from "react";

function App() {
  const [selectedVideo, setSelectedVideo] = useState("video1");

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>🎥 Multi-Video Player</h1>

      <select
        value={selectedVideo}
        onChange={(e) => setSelectedVideo(e.target.value)}
        style={{ marginBottom: "20px", fontSize: "16px", padding: "8px" }}
      >
        <option value="video1">Nature Video</option>
        <option value="video2">Ocean Scenery</option>
        <option value="video3">Forest Walk</option>
      </select>

      <div>
        <video width="800" controls key={selectedVideo}>
          <source
            src={`http://localhost:5000/video/${selectedVideo}`}
            type="video/mp4"
          />
          Your browser does not support the video tag.
        </video>
      </div>
    </div>
  );
}

export default App;
