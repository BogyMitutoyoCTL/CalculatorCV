import cv2
from PictureStorage import PictureStorage
from Button import Button

class ButtonGenerator:
    def __init__(self, picture_storage: PictureStorage):
        self.picture = picture_storage.get_picture(0)
        self.width = len(self.picture[0])
        self.hight = len(self.picture)

    def addieren(self):

        x = self.width
        y = self.hight

        top_x = x // 11
        top_y = y // 11
        bottom_x = x // 11 * 4
        bottom_y = y // 11 * 4
        text = "+"

        return Button(top_x, top_y, bottom_x, bottom_y, text)

    def subtrahieren(self):

        x = self.width
        y = self.hight

        top_x = x // 11 * 6
        top_y = y // 11
        bottom_x = x // 11 * 9
        bottom_y = y // 11 * 4
        text = "-"

        return Button(top_x, top_y, bottom_x, bottom_y, text)

    def multiplizieren(self):

        x = self.width
        y = self.hight

        top_x = x // 11
        top_y = y // 11 * 6
        bottom_x = x // 11 * 4
        bottom_y = y // 11 * 9
        text = "*"

        return Button(top_x, top_y, bottom_x, bottom_y, text)

    def dividieren(self,):

        x = self.width
        y = self.hight

        top_x = x // 11 * 6
        top_y = y // 11 * 6
        bottom_x = x // 11 * 9
        bottom_y = y // 11 * 9
        text = "/"

        return Button(top_x, top_y, bottom_x, bottom_y, text)

    def draw_all_buttons(self):

        return [self.addieren(), self.subtrahieren(), self.multiplizieren(), self.dividieren()]