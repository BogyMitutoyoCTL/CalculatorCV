import cv2

class Bildbearbeitungstools():
    def __init__(self, bildspeicher, datenbank):
        self.bildspeicher = bildspeicher
        self.datenbank = datenbank

    def convert_brg2hsv(self):
        bgr_bild = self.bildspeicher.get_bild(self.bildspeicher.BGR)
        hsv_bild = cv2.cvtColor(bgr_bild, cv2.COLOR_BGR2HSV)
        self.bildspeicher.add_bild(hsv_bild, self.bildspeicher.HSV)

    def glove_filter(self):
        lowerhsv = (self.datenbank.lower_h, self.datenbank.lower_s, self.datenbank.lower_v)
        upperhsv = (self.datenbank.upper_h, self.datenbank.upper_s, self.datenbank.upper_v)
        hsv_bild = self.bildspeicher.get_bild(self.bildspeicher.HSV)
        self.bildspeicher.add_bild(cv2.inRange(hsv_bild, lowerhsv, upperhsv), self.bildspeicher.GRAY)
