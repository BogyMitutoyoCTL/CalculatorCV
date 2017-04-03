from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


class Picture:

    def __init__(self):
        self.image = None

    def show_picture(self, fenster_name, bild):
        camera.capture(bild, format="bgr")
        self.image = bild.array
        cv2.imshow(fenster_name, self.image)

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

Bild = Picture()
Bild.show_picture("Bild", rawCapture)
cv2.waitKey(0)
