import cv2

class Feld:
    def __init__(self, feldx1, feldx2, feldy1, feldy2, bildspeicher):
        self.punkt1 = (feldx1, feldy1)
        self.punkt2 = (feldx2, feldy2)
        #self.background = picture
        self.bildspeicher = bildspeicher
        self.color = (255, 255, 255)

    def draw_feld(self, index):
        bild_mit_feld = cv2.rectangle(self.bildspeicher.get_picture(index), self.punkt1, self.punkt2, self.color)
        self.bildspeicher.add_picture_mit_felder(bild_mit_feld, index)

    def set_punkt_1_x(self, wert):
        self.punkt1 = (wert, self.punkt1[0])

    def set_punkt_2_x(self, wert):
        self.punkt2 = (wert, self.punkt2[0])

    def set_punkt_1_y(self, wert):
        self.punkt1 = (self.punkt1[0], wert)

    def set_punkt_2_y(self, wert):
        self.punkt2 = (self.punkt2[0], wert)

    def set_color(self, color):
        self.color = color

    def get_punkt_1_x(self):
        return self.punkt1[0]

    def get_punkt_1_y(self):
        return self.punkt1[1]

    def get_punkt_2_x(self):
        return self.punkt2[0]

    def get_punkt_2_y(self):
        return self.punkt2[1]

    def get_color(self):
        return self.color

