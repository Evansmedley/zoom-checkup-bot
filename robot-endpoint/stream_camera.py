import cv2
from threading import Condition
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import threading

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

                self.send_frame(frame)

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


class StreamingServer(socketserver.ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def opencv_camera_stream():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        with output.condition:
            output.condition.notify_all()

        cv2.imshow('Camera Stream', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    output = StreamingOutput()

    server_process = StreamingServer(('0.0.0.0', 8000), StreamingHandler)
    server_thread = threading.Thread(target=server_process.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    opencv_camera_stream()
