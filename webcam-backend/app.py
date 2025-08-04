from flask import Flask, Response, request
from flask_cors import CORS
import cv2

app = Flask(__name__)
CORS(app)

RTSP_URL = "rtsp://10.129.2.138:554/main_stream"
streaming = {"active": True}

def generate_frames():
    cap = cv2.VideoCapture(RTSP_URL)
    if not cap.isOpened():
        raise RuntimeError("Cannot open RTSP stream.")

    while streaming["active"]:
        success, frame = cap.read()
        if not success:
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    streaming["active"] = True
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stop_stream', methods=['POST'])
def stop_stream():
    streaming["active"] = False
    return {"message": "Streaming stopped"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
