from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


class Picture:

    def __init__(self, bildspeicher):
        self.image = None
        self.bildspeicher = bildspeicher
        self.camera = PiCamera()
        self.rawCapture = PiRGBArray(self.camera)

        time.sleep(0.1)

    def save_picture(self):
        self.camera.capture(self.rawCapture, format="bgr")
        self.image = self.rawCapture.array
        self.bildspeicher.add_bild(self.image, 0)

