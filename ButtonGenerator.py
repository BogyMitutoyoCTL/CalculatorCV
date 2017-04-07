from PictureStorage import PictureStorage
from Button import Button


class ButtonGenerator:
    def __init__(self, picture_storage: PictureStorage):
        self.picture_storage = picture_storage
        self.width = None
        self.height = None
        self.section_count = 15
        self.default_button_size = 3
        self.margin = 1
        self.text_scale = 3
        self.text_scale_del = 1

    def add_size(self):
        picture = self.picture_storage.get_picture(0)
        self.width = len(picture[0])
        self.height = len(picture)

    def create_add_button(self) -> Button:
        top_x = self.from_left(1)
        top_y = self.from_top(1)
        bottom_x = self.calculate_bottom(top_x, self.width, self.default_button_size)
        bottom_y = self.calculate_bottom(top_y, self.height, self.default_button_size)
        text = "+"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def create_subtract_button(self) -> Button:
        top_x = self.from_right()
        top_y = self.from_top(1)
        bottom_x = self.calculate_bottom(top_x, self.width, self.default_button_size)
        bottom_y = self.calculate_bottom(top_y, self.height, self.default_button_size)
        text = "-"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def create_multiply_button(self) -> Button:
        top_x = self.from_left(1)
        top_y = self.from_bottom()
        bottom_x = self.calculate_bottom(top_x, self.width, self.default_button_size)
        bottom_y = self.calculate_bottom(top_y, self.height, self.default_button_size)
        text = "*"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale)

    def create_delete_button(self) -> Button:
        top_x = self.from_left(5)
        top_y = self.from_bottom()
        bottom_x = self.calculate_bottom(top_x, self.width, 5)
        bottom_y = self.calculate_bottom(top_y, self.height, self.default_button_size)

        text = "delete"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale_del)

    def create_divide_button(self) -> Button:
        top_x = self.from_right()
        top_y = self.from_bottom()
        bottom_x = self.calculate_bottom(top_x, self.width, self.default_button_size)
        bottom_y = self.calculate_bottom(top_y, self.height, self.default_button_size)
        text = "/"

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale_del)

    def calculation_field(self) -> Button:
        top_x = self.from_left(5)
        top_y = self.from_top(1)
        bottom_x = self.calculate_bottom(top_x, self.width, 5)
        bottom_y = self.calculate_bottom(top_y, self.height, self.default_button_size)
        text = ""

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale_del)

    def choosing_field(self) -> Button:
        top_x = self.from_left(4)
        top_y = self.from_top(4)
        bottom_x = self.calculate_bottom(top_x, self.width, 7)
        bottom_y = self.calculate_bottom(top_y, self.height, 7)

        text = ""

        return Button(top_x, top_y, bottom_x, bottom_y, text, self.text_scale_del)

    def generate_all_buttons(self) -> [Button]:
        return [self.create_add_button(),
                self.create_subtract_button(),
                self.create_multiply_button(),
                self.create_delete_button(),
                self.create_divide_button(),
                self.choosing_field(),
                self.calculation_field()]

    def from_top_left(self, x, count) -> int:
        return x // self.section_count * self.margin * count

    def from_top(self, count) -> int:
        return self.from_top_left(self.height, count)

    def from_left(self, count) -> int:
        return self.from_top_left(self.width, count)

    def from_bottom_right(self, x) -> int:
        return x // self.section_count * (self.section_count - self.default_button_size - self.margin)

    def from_bottom(self) -> int:
        return self.from_bottom_right(self.height)

    def from_right(self) -> int:
        return self.from_bottom_right(self.width)

    def calculate_bottom(self, top_x, x, button_width) -> int:
        return top_x + button_width * x // self.section_count
