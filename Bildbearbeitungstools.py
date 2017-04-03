import Bildspeicher
import cv2

class Bildbearbeitungstools():
    def __init__(self, bildspeicher):
        self.bildspeicher = bildspeicher

    def convert_brg2hsv(self):
        self.bildspeicher.add_bild(cv2.cvtColor(self.bildspeicher.get_bild(0), cv2.COLOR_BGR2HSV), 1)

