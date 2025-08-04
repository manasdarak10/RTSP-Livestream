from flask import Flask, Response
import cv2

app = Flask(__name__)

# Replace with your RTSP stream
RTSP_URL = "Enter your URL here"

def generate_frames():
    cap = cv2.VideoCapture(RTSP_URL)

    if not cap.isOpened():
        raise RuntimeError("Failed to open RTSP stream.")

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Encode frame to JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield MJPEG frame
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return '''<html><body><h1>RTSP Stream</h1><img src="/video_feed"></body></html>'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
