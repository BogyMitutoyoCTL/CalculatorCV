import cv2

Haupt_x = 1280                     #wie bekomme ich die Information aus dem Bild?
Haupt_y = 720



class Felder:
    def __init__(self, input):

        self.picture = input

    def addieren(self, x, y):

        if y < x:
            r = y // 8
        else:
            r = x // 8

        self.picture = cv2.circle(self.picture, (x // 6, y // 6), r, (255, 69,0))
        self.picture = cv2.putText(self.picture, "+", (), cv2.FONT_HERSHEY_SIMPLEX, 11, (0, 0, 0))

    def subtrahieren(self, x, y):

        if y < x:
            r = y // 8
        else:
            r = x // 8

        self.picture = cv2.circle(self.picture, (x // 6 * 5, y // 6), r, (255, 69, 0))
        self.picture = cv2.putText(self.picture, "-", (), cv2.FONT_HERSHEY_SIMPLEX, 11, (0, 0, 0))

    def multiplizieren(self, x, y):

        if y < x:
            r = y // 8
        else:
            r = x // 8

        self.picture = cv2.circle(self.picture, (x // 6, y // 6 * 5), r, (255, 69, 0))
        self.picture = cv2.putText(self.picture, "*", (), cv2.FONT_HERSHEY_SIMPLEX, 11, (0, 0, 0))

    def dividieren(self, x, y):

        if y < x:
            r = y // 8
        else:
            r = x // 8

        self.picture = cv2.circle(self.picture, (x // 6 * 5, y // 6 * 5), r, (255, 69, 0))
        self.picture = cv2.putText(self.picture, "/", (), cv2.FONT_HERSHEY_SIMPLEX, 11, (0, 0, 0))

    def waitKey(self):

        cv2.waitKey(0) & 0xFF

test = Felder("white.png")
test.addieren(Haupt_x, Haupt_y)
test.subtrahieren(Haupt_x, Haupt_y)
test.multiplizieren(Haupt_x, Haupt_y)
test.dividieren(Haupt_x, Haupt_y)