import platform
import time
import cv2
import numpy

systemIsWindows = platform.system()[0:5] != "Linux"
if not systemIsWindows:
        from picamera.array import PiRGBArray
        from picamera import PiCamera

LITTLE_COLOR = 10


class Camera:

    def __init__(self):
        if systemIsWindows:
            self.camera = WindowsCamera()
        else:
            self.camera = LinuxCamera()

        time.sleep(0.1)
        if not(self.camera_is_available()):
            raise RuntimeError("No camera is available. Is the program already running?")

    def get_picture(self):
        return self.camera.get_next_frame()

    def camera_is_available(self):
        image = self.camera.get_next_frame()

        # If we do not get anything, probably no camera is connected
        if image is None:
            return False

        # Check for black image (program started twice)
        if self._is_mostly_black(image):
            return False

        return True

    @staticmethod
    def _is_mostly_black(frame):
        average_color_per_row = numpy.average(frame, axis=0)
        average_color = numpy.average(average_color_per_row, axis=0)
        if average_color[0] < LITTLE_COLOR and average_color[1] < LITTLE_COLOR and average_color[2] < LITTLE_COLOR:
            return True

        return False


DEFAULT_CAMERA = 1
RESOLUTION = (1280, 720)
FRAMERATE = 30


class WindowsCamera:
    def __init__(self):
        self.camera = cv2.VideoCapture(DEFAULT_CAMERA)
        self.camera.set(cv2.CAP_PROP_FPS, FRAMERATE)
        width, height = RESOLUTION
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.camera.set(cv2.CAP_PROP_CONVERT_RGB, False)  # leave in BGR mode

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
