# 🖥️ React + Flask Webcam Streamer

This project combines a **React frontend** with a **Flask + OpenCV backend** to stream live webcam footage from your local machine to a website in real time.

---

## 📸 Features

- Live webcam video streamed directly using OpenCV.
- Backend powered by Flask.
- Frontend built with React and fetches the webcam stream.
- Cross-Origin support (CORS) to enable communication between frontend and backend.
- Local development setup with clean architecture.

---

## 🧾 Folder Structure

```
Main/  
├── react-webcam-site/      # React frontend  
├── webcam-backend/         # Flask backend  
```

---

## 🚀 Getting Started

### 1. Clone the Repository & Navigate

```bash
git clone https://github.com/YOUR_USERNAME/react-flask-webcam.git
cd react-flask-webcam
```

---

### 2. Backend Setup (Flask + OpenCV)

```bash
cd webcam-backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Your webcam stream will be available at `http://localhost:5000/video`

---

### 3. Frontend Setup (React)

```bash
cd ../react-webcam-site
npm install
npm start
```

The React app will run on `http://localhost:3000` and show the webcam stream.

---

## ⚙️ Tech Stack

- **Frontend**: React, JavaScript  
- **Backend**: Python, Flask, OpenCV  
- **Streaming**: MJPEG via Flask `Response()`  
- **Communication**: CORS enabled

---

## 🛡️ Notes

- Works only with a local webcam (`cv2.VideoCapture(0)`)
- Do not upload `node_modules/` or `venv/` to GitHub — use `.gitignore`
- Tested on Windows 10/11 with Python 3.12 and Node.js 18+

---

