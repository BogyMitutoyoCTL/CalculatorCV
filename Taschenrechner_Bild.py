import time
import platform
import time
import cv2

systemIsWindows = platform.system()[0:5] != "Linux"
if not systemIsWindows:
        from picamera.array import PiRGBArray
        from picamera import PiCamera


class Picture:

    def __init__(self, bildspeicher):
        self.image = None
        self.bildspeicher = bildspeicher
        if systemIsWindows:
            self.camera = WindowsCamera()
        else:
            self.camera = LinuxCamera()

        time.sleep(0.1)

    def save_picture(self):
        self.image = self.camera.get_next_frame()
        self.bildspeicher.add_bild(self.image, self.bildspeicher.BGR)


DEFAULT_CAMERA = 0
RESOLUTION = (800, 800)
FRAMERATE = 120


class WindowsCamera:
    def __init__(self):
        self.camera = cv2.VideoCapture(DEFAULT_CAMERA)

    def get_next_frame(self):
        _, frame = self.camera.read()
        return frame


class LinuxCamera:
    def __init__(self):
        self.camera = PiCamera(resolution=RESOLUTION, framerate=FRAMERATE)
        self.rawCapture = PiRGBArray(self.camera, size=RESOLUTION)
        time.sleep(0.1)

    def get_next_frame(self):
        self.camera.capture(self.rawCapture, format="bgr", use_video_port=True)
        frame = self.rawCapture.array
        self.rawCapture.truncate(0)
        return frame
