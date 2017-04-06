import cv2
from PictureStorage import PictureStorage
from Button import Button


class ButtonGenerator:
    def __init__(self, picture_storage: PictureStorage):
        self.picture = picture_storage.get_picture(0)
        self.width = len(self.picture[0])
        self.hight = len(self.picture)
        self.section_count = 15

    def addieren(self):

        x = self.width
        y = self.hight

        top_x = x // self.section_count
        top_y = y // self.section_count
        bottom_x = top_x + 3 * x // self.section_count
        bottom_y = top_y + 3 * y // self.section_count
        text = "+"

        return Button(top_x, top_y, bottom_x, bottom_y, text, 3)

    def subtrahieren(self):

        x = self.width
        y = self.hight

        top_x = x // self.section_count * (self.section_count - 3 - 1)
        top_y = y // self.section_count
        bottom_x = top_x + 3 * x // self.section_count
        bottom_y = top_y + 3 * y // self.section_count
        text = "-"

        return Button(top_x, top_y, bottom_x, bottom_y, text, 3)

    def multiplizieren(self):

        x = self.width
        y = self.hight

        top_x = x // self.section_count
        top_y = y // self.section_count * (self.section_count - 3 -1)
        bottom_x = top_x + 3 * x // self.section_count
        bottom_y = top_y + 3 * y // self.section_count
        text = "*"

        return Button(top_x, top_y, bottom_x, bottom_y, text, 3)

    def delete(self,):

        x = self.width
        y = self.hight

        top_x = x // self.section_count * (self.section_count - 3 -1)
        top_y = y // self.section_count * (self.section_count - 3 -1)
        bottom_x = top_x + 3 * x // self.section_count
        bottom_y = top_y + 3 * y // self.section_count
        text = "delete"

        return Button(top_x, top_y, bottom_x, bottom_y, text, 1)

    def draw_all_buttons(self):

        return [self.addieren(), self.subtrahieren(), self.multiplizieren(), self.delete()]