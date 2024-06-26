import cv2
from threading import Condition
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import threading
import logging

HTML_PAGE = """
<html>
<head>
<title>Camera Stream</title>
</head>
<body>
    <center><h1>Camera Stream</h1></center>
    <center><img src="stream.mjpg" width="720" height="530"></center>
</body>
</html>
"""

class StreamingOutput:
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, frame):
        with self.condition:
            self.frame = frame
            self.condition.notify_all()

output = StreamingOutput()

class StreamingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(HTML_PAGE))
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode('utf-8'))
        elif self.path == '/stream.mjpg':
            self.handle_mjpeg_stream()
        else:
            self.send_error(404)
            self.end_headers()

    def handle_mjpeg_stream(self):
        self.send_response(200)
        self.send_header('Age', 0)
        self.send_header('Cache-Control', 'no-cache, private')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
        self.end_headers()

        try:
            while True:
                with output.condition:
                    output.condition.wait()
                    frame = output.frame

                _, jpeg = cv2.imencode('.jpg', frame)
                self.wfile.write(b'--FRAME\r\n')
                self.send_header('Content-Type', 'image/jpeg')
                self.send_header('Content-Length', len(jpeg))
                self.end_headers()
                self.wfile.write(jpeg.tobytes())
                self.wfile.write(b'\r\n')

        except Exception as e:
            logging.warning(f'Removed streaming client {self.client_address}: {str(e)}')

    def send_frame(self, frame):
        _, jpeg = cv2.imencode('.jpg', frame)
        self.wfile.write(b'--FRAME\r\n')
        self.send_header('Content-Type', 'image/jpeg')
        self.send_header('Content-Length', len(jpeg))
        self.end_headers()
        self.wfile.write(jpeg.tobytes())
        self.wfile.write(b'\r\n')

def follow_function(img, mouthDetect):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = mouthDetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cv2.putText(img, 'Mouth', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (105, 105, 105), 2)

    return img

class StreamingServer(socketserver.ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

def opencv_camera_stream():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Load mouth cascade classifier
    mouthDetect = cv2.CascadeClassifier("haarcascade_mouth.xml")

    try:
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Error: Failed to capture frame.")
                break

            # Apply follow_function for mouth detection
            frame = follow_function(frame, mouthDetect)

            with output.condition:
                output.frame = frame
                output.condition.notify_all()

            cv2.imshow('Camera Stream', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        server_process = StreamingServer(('0.0.0.0', 5000), StreamingHandler)
        server_thread = threading.Thread(target=server_process.serve_forever)
        server_thread.daemon = True
        server_thread.start()

        opencv_camera_stream()

    except KeyboardInterrupt:
        print("Interrupted. Stopping server and releasing resources.")
        server_process.shutdown()
        server_process.server_close()
        cv2.destroyAllWindows()
        exit()
