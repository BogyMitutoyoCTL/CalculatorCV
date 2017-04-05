import cv2

class ButtonGenerator:
    def __init__(self, picture):
        self.picture = picture
        self.x = len(self.picture[0])
        self.y = len(self.picture)
        self.MitutoyoFarbe = (54, 120, 244)

    def generate(self):
        # TODO: Liste mit 4 Buttons erzeugen und zurückgeben (paul)
        pass

    def addieren(self):

        x = self.x
        y = self.y

        top_x = x // 11
        top_y = x // 11
        bottom_x = x // 10 * 4
        bottom_y = y // 10 * 4
        text = "+"

        return top_x, top_y, bottom_x, bottom_y, text

    def subtrahieren(self):

        x = self.x
        y = self.y

        top_x = x // 11 * 6
        top_y = x // 11
        bottom_x = x // 10 * 9
        bottom_y = y // 10 * 4
        text = "-"

        return top_x, top_y, bottom_x, bottom_y, text

    def multiplizieren(self):

        x = self.x
        y = self.y

        top_x = x // 11
        top_y = x // 11 * 6
        bottom_x = x // 10 * 4
        bottom_y = y // 10 * 9
        text = "*"

        return top_x, top_y, bottom_x, bottom_y, text

    def dividieren(self,):

        x = self.x
        y = self.y

        top_x = x // 11 * 6
        top_y = x // 11 * 6
        bottom_x = x // 10 * 9
        bottom_y = y // 10 * 9
        text = "/"

        return top_x, top_y, bottom_x, bottom_y, text