import cv2
from PictureStorage import PictureStorage
from Button import Button


class ButtonGenerator:
    def __init__(self, picture_storage: PictureStorage):
        self.picture = picture_storage.get_picture(0)
        self.width = len(self.picture[0])
        self.hight = len(self.picture)
        self.section_count = 15
        self.button_size = 3
        self.margin = 1
        self.text_scale = 3
        self.text_scale_del = 1

    def addieren(self):
        x = self.width
        y = self.hight

        top_x = self.from_top_left(x)
        top_y = self.from_top_left(y)
        bottom_x = self.calculate_bottom(top_x, x)
        bottom_y = self.calculate_bottom(top_y, y)
        text = "+"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def subtrahieren(self):

        x = self.width
        y = self.hight

        top_x = self.from_bottom_right(x)
        top_y = self.from_top_left(y)
        bottom_x = self.calculate_bottom(top_x, x)
        bottom_y = self.calculate_bottom(top_y, y)
        text = "-"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def multiplizieren(self):

        x = self.width
        y = self.hight


        top_x = self.from_top_left(x)
        top_y = self.from_bottom_right(y)
        bottom_x = self.calculate_bottom(top_x, x)
        bottom_y = self.calculate_bottom(top_y, y)
        text = "*"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def from_top_left(self, x):
        return x // self.section_count * self.margin

    def delete(self,):
        x = self.width
        y = self.hight

        top_x = self.from_bottom_right(x)
        top_y = self.from_bottom_right(y)
        bottom_x = self.calculate_bottom(top_x, x)
        bottom_y = self.calculate_bottom(top_y, y)
        text = "delete"


        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale_del)

    def draw_all_buttons(self):
        return [self.addieren(), self.subtrahieren(), self.multiplizieren(), self.delete()]

    def from_bottom_right(self, x):
        return x // self.section_count * (self.section_count - self.button_size - self.margin)

    def calculate_bottom(self, top_x, x):
        return top_x + self.button_size * x // self.section_count