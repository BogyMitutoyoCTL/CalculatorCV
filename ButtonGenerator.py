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
        top_x = self.from_left()
        top_y = self.from_top()
        bottom_x = self.calculate_bottom(top_x, self.width)
        bottom_y = self.calculate_bottom(top_y, self.hight)
        text = "+"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def subtrahieren(self):
        top_x = self.from_right()
        top_y = self.from_top()
        bottom_x = self.calculate_bottom(top_x, self.width)
        bottom_y = self.calculate_bottom(top_y, self.hight)
        text = "-"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def multiplizieren(self):
        top_x = self.from_left()
        top_y = self.from_bottom()
        bottom_x = self.calculate_bottom(top_x, self.width)
        bottom_y = self.calculate_bottom(top_y, self.hight)
        text = "*"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def delete(self):
        top_x = self.from_right()
        top_y = self.from_bottom()
        bottom_x = self.calculate_bottom(top_x, self.width)
        bottom_y = self.calculate_bottom(top_y, self.hight)
        text = "delete"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale_del)

    def draw_all_buttons(self):
        return [self.addieren(), self.subtrahieren(), self.multiplizieren(), self.delete()]

    def from_top_left(self, x):
        return x // self.section_count * self.margin

    def from_top(self):
        return self.from_top_left(self.hight)

    def from_left(self):
        return self.from_top_left(self.width)

    def from_bottom_right(self, x):
        return x // self.section_count * (self.section_count - self.button_size - self.margin)

    def from_bottom(self):
        return self.from_bottom_right(self.hight)

    def from_right(self):
        return self.from_bottom_right(self.width)


    def calculate_bottom(self, top_x, x):
        return top_x + self.button_size * x // self.section_count