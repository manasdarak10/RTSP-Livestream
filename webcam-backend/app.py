from flask import Flask, Response, send_file
from flask_cors import CORS
import cv2

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Dictionary of available videos
VIDEOS = {
    "video1": "naturevideo.mp4",
    "video2": "oceanscenery.mp4",
    "video3": "forestwalk.mp4"
}

# MJPEG code — not used in your current video player
camera = cv2.VideoCapture("naturevideo.mp4")

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            )

# Default video route (optional now)
@app.route('/video')
def video():
    return send_file("naturevideo.mp4", mimetype='video/mp4')

# ✅ ADD THIS NEW ROUTE for multiple videos
@app.route('/video/<video_id>')
def get_video(video_id):
    video_path = VIDEOS.get(video_id)
    if video_path:
        return send_file(video_path, mimetype='video/mp4')
    else:
        return "Video not found", 404

@app.route('/')
def home():
    return "Webcam server is running."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
