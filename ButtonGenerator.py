import cv2

class ButtonGenerator:
    def __init__(self, picture):
        self.picture = picture
        self.x = len(self.picture[0])
        self.y = len(self.picture)
        self.MitutoyoFarbe = (54, 120, 244)

    def generate(self):
        # TODO: Liste mit 4 Buttons erzeugen und zurückgeben
        pass

    def addieren(self):

        x = self.x
        y = self.y

        cv2.rectangle(self.picture, (x // 10, y // 10), (x // 10 * 4, y // 10 * 4), self.MitutoyoFarbe, 5)
        cv2.putText(self.picture, "+", (x // 10 * 2, y // 10 * 3), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2)

    def subtrahieren(self):

        x = self.x
        y = self.y

        cv2.rectangle(self.picture, (x // 10 * 6, y // 10), (x // 10 * 9, y // 10 * 4), self.MitutoyoFarbe, 5)
        cv2.putText(self.picture, "-", (x // 10 * 7, y // 10 * 3), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2)

    def multiplizieren(self):

        x = self.x
        y = self.y

        cv2.rectangle(self.picture, (x // 10, y // 10 * 6), (x // 10 * 4, y // 10 * 9), self.MitutoyoFarbe, 5)
        cv2.putText(self.picture, "*", (x // 10 * 2, y // 10 * 8), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2)

    def dividieren(self,):

        x = self.x
        y = self.y

        cv2.rectangle(self.picture, (x // 10 * 6, y // 10 * 6), ( x // 10 * 9, y // 10 * 9), self.MitutoyoFarbe, 5)
        cv2.putText(self.picture, "/", (x // 10 * 7, y // 10 * 8), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)