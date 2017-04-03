import cv2

class Bildbearbeitungstools():
    def __init__(self, bildspeicher):
        self.bildspeicher = bildspeicher

    def convert_brg2hsv(self):
        bgr_bild = self.bildspeicher.get_bild(self.bildspeicher.BGR)
        hsv_bild = cv2.cvtColor(bgr_bild, cv2.COLOR_BGR2HSV)
        self.bildspeicher.add_bild(hsv_bild, self.bildspeicher.HSV)


