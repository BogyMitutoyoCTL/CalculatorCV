import cv2

class Felder:
    def __init__(self, filename):

        self.picture = cv2.imread(filename)
        self.x = len(self.picture[0])
        self.y = len(self.picture)
        self.MitutoyoFarbe = (54, 120, 244)


        self.windowName = None
        cv2.namedWindow(self.windowName)

    def addieren(self):

        x = self.x
        y = self.y

        cv2.rectangle(self.picture, (x // 10, y // 10), (x // 10 * 4, y // 10 * 4), self.MitutoyoFarbe, 5)
        cv2.putText(self.picture, "+", (x // 10 * 2, y // 10 * 2), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2)

    def subtrahieren(self):

        x = self.x
        y = self.y

        cv2.rectangle(self.picture, (x // 10 * 6, y // 10), (x // 10 * 9, y // 10 * 4), self.MitutoyoFarbe, 5)
        cv2.putText(self.picture, "-", (x // 10 * 7, y // 10 * 2), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2)

    def multiplizieren(self):

        x = self.x
        y = self.y

        cv2.rectangle(self.picture, (x // 10, y // 10 * 6), (x // 10 * 4, y // 10 * 9), self.MitutoyoFarbe, 5)
        cv2.putText(self.picture, "*", (x // 10 * 2, y // 10 * 7), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2)

    def dividieren(self,):

        x = self.x
        y = self.y

        if y < x:
            r = y // 8
        else:
            r = x // 8

        cv2.rectangle(self.picture, (x // 10 * 6, y // 10 * 6), ( x // 10 * 9, y // 10 * 9), self.MitutoyoFarbe, 5)
        cv2.putText(self.picture, "/", (x // 10 * 7, y // 10 * 7), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)

    def show_image(self):

        cv2.imshow(self.windowName, self.picture)

    def waitKey(self):

        cv2.waitKey(0) & 0xFF


test = Felder("white.png")
test.addieren()
test.subtrahieren()
test.multiplizieren()
test.dividieren()
test.show_image()
test.waitKey()