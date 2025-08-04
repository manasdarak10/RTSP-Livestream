import React, { useState } from "react";

function App() {
  const [streaming, setStreaming] = useState(true);

  const handleStopStream = async () => {
    try {
      await fetch("http://localhost:5000/stop_stream", {
        method: "POST",
      });
      alert("Live stream stopped.");
      setStreaming(false);
    } catch (error) {
      alert("Error stopping stream.");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>📡 RTSP Live Stream</h1>

      {streaming ? (
        <>
          <img
            src="http://localhost:5000/video_feed"
            alt="Live RTSP Stream"
            width="800"
            style={{ border: "2px solid #333" }}
          />
          <br />
          <button
            onClick={handleStopStream}
            style={{
              marginTop: "15px",
              padding: "10px 20px",
              fontSize: "16px",
              backgroundColor: "#e53935",
              color: "white",
              border: "none",
              borderRadius: "5px",
              cursor: "pointer",
            }}
          >
            🛑 Stop Stream
          </button>
        </>
      ) : (
        <p style={{ fontSize: "18px", marginTop: "30px" }}>
          🔴 Stream has been stopped.
        </p>
      )}
    </div>
  );
}

export default App;
