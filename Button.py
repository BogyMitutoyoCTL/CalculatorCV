import cv2
from typing import Tuple


class Button:
    def __init__(self, top_x: int, top_y: int, bottom_x: int, bottom_y: int, text: str, scale):
        self.top_left = (top_x, top_y)
        self.bottom_right = (bottom_x, bottom_y)
        self.top_x = top_x
        self.top_y = top_y
        self.bottom_x = bottom_x
        self.bottom_y = bottom_y
        self.total_x = self.top_x + self.bottom_x
        self.total_y = self.top_y + self.bottom_y
        self.text = text
        self.color = (54, 120, 244)
        self.text_shape = cv2.FONT_HERSHEY_SIMPLEX
        self.scale = scale
        self.thickness_rect = 5
        self.thickness_text = 2

    def draw_field(self, picture):
        picture = picture.copy()
        cv2.rectangle(picture, self.top_left, self.bottom_right, self.color, self.thickness_rect)

        text_size = cv2.getTextSize(self.text, self.text_shape, self.scale, self.thickness_text)
        width = text_size[0][0]
        height = text_size[0][1]

        x = self.total_x // 2 - width // 2
        y = self.total_y // 2 + height // 2

        cv2.putText(picture, self.text, (x, y), self.text_shape, self.scale, self.color, self.thickness_text)

        return picture

    def get_top_x(self) -> int:
        return self.top_left[0]

    def get_top_y(self) -> int:
        return self.top_left[1]

    def get_bottom_x(self) -> int:
        return self.bottom_right[0]

    def get_bottom_y(self) -> int:
        return self.bottom_right[1]

    def contains_point(self, point: Tuple[int, int]) -> bool:
        return self.top_x <= point[0] <= self.bottom_x and self.top_y <= point[1] <= self.bottom_y
