import cv2

class Feld:
    def __init__(self, feldx1, feldx2, feldy1, feldy2, picture, bildspeicher):
        self.punkt1 = (feldx1, feldy1)
        self.punkt2 = (feldx2, feldy2)
        self.background = picture
        self.bildspeicher = bildspeicher
        self.color = (255, 255, 255)

    def draw_feld(self):
        bild_mit_feld = cv2.rectangle(self.bildspeicher.get_bild(self.bildspeicher.BGR), self.punkt1, self.punkt2,self.color)
        self.bildspeicher.add_bild_mit_felder(bild_mit_feld, self.bildspeicher.BGR)
