from PictureStorage import PictureStorage
from Button import Button


class ButtonGenerator:
    def __init__(self, picture_storage: PictureStorage):
        self.picture = picture_storage.get_picture(0)
        self.width = len(self.picture[0])
        self.hight = len(self.picture)
        self.section_count = 15
        self.default_button_size = 3
        self.margin = 1
        self.text_scale = 3
        self.text_scale_del = 1

    def addieren(self):
        top_x = self.from_left(1)
        top_y = self.from_top(1)
        bottom_x = self.calculate_bottom(top_x, self.width, self.default_button_size)
        bottom_y = self.calculate_bottom(top_y, self.hight, self.default_button_size)
        text = "+"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def subtrahieren(self):
        top_x = self.from_right()
        top_y = self.from_top(1)
        bottom_x = self.calculate_bottom(top_x, self.width, self.default_button_size)
        bottom_y = self.calculate_bottom(top_y, self.hight, self.default_button_size)
        text = "-"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def multiplizieren(self):
        top_x = self.from_left(1)
        top_y = self.from_bottom()
        bottom_x = self.calculate_bottom(top_x, self.width, self.default_button_size)
        bottom_y = self.calculate_bottom(top_y, self.hight, self.default_button_size)
        text = "*"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def delete(self):

        top_x = self.from_left(5)
        top_y = self.from_bottom()
        bottom_x = self.calculate_bottom(top_x, self.width, 5)
        bottom_y = self.calculate_bottom(top_y, self.hight, self.default_button_size)

        text = "delete"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale_del)

    def division(self):
        top_x = self.from_right()
        top_y = self.from_bottom()
        bottom_x = self.calculate_bottom(top_x, self.width, self.default_button_size)
        bottom_y = self.calculate_bottom(top_y, self.hight, self.default_button_size)
        text = "/"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale_del)

    def calculation_field(self):
        top_x = self.from_left(5)
        top_y = self.from_top(1)
        bottom_x = self.calculate_bottom(top_x, self.width, 5)
        bottom_y = self.calculate_bottom(top_y, self.hight, self.default_button_size)
        text = None

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale_del)

    def choosing_field(self):
        top_x = self. from_left(4)
        top_y = self.from_top(4)
        bottom_x = self.calculate_bottom(top_x, self.width, 7)
        bottom_y = self.calculate_bottom(top_y, self.hight, 7)

        text = None

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale_del)

    def generate_all_buttons(self):
        return [self.addieren(), self.subtrahieren(), self.multiplizieren(), self.delete(), self.division(), self.choosing_field(), self.calculation_field()]

    def from_top_left(self, x, count):
        return x // self.section_count * self.margin * count

    def from_top(self, count):
        return self.from_top_left(self.hight, count)

    def from_left(self, count):
        return self.from_top_left(self.width, count)

    def from_bottom_right(self, x):
        return x // self.section_count * (self.section_count - self.default_button_size - self.margin)

    def from_bottom(self):
        return self.from_bottom_right(self.hight)

    def from_right(self):
        return self.from_bottom_right(self.width)


    def calculate_bottom(self, top_x, x, button_width):
        return top_x + button_width * x // self.section_count