import cv2

class Feld:

    def feld_erkennung(self, feldx1, feldx2, feldy1, feldy2, handx, handy):
        return feldx1 <= handx <= feldx2 and feldy1 <= handy <= feldy2

