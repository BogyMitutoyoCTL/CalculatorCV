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

    def color_glove(self):
        umgedreht = cv2.bitwise_not(self.bildspeicher.get_bild(self.bildspeicher.GRAY2))
        source = self.bildspeicher.get_bild(self.bildspeicher.BGR)
        bgr2_bild = cv2.bitwise_and(source, 1, source, umgedreht)
        self.bildspeicher.add_bild(bgr2_bild, self. bildspeicher.BGR2)

    def blur(self, breite, höhe):
        blur_bild = cv2.blur(self.bildspeicher.get_bild(self.bildspeicher.GRAY), (breite, höhe))
        blurgray_bild = cv2.inRange(blur_bild, (100), (255))
        self.bildspeicher.add_bild(blurgray_bild, self.bildspeicher.GRAY2)