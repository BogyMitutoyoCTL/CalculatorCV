import cv2
from PictureStorage import PictureStorage


class Button:
    def __init__(self, top_x: int, top_y: int, bottom_x: int, bottom_y: int, text: str):
        self.top_left = (top_x, top_y)
        self.bottom_right = (bottom_x, bottom_y)
        self.color = (54, 120, 244)
        self.thickness = 5
        self.text = text
        self.top_x = top_x
        self.top_y = top_y
        self.bottom_x = bottom_x
        self.bottom_y = bottom_y


    def draw_field(self, picture):
        picture = picture.copy()
        picture = cv2.rectangle(picture, self.top_left, self.bottom_right, self.color, self.thickness)

        x = (self.top_x + self.bottom_x) // 2
        y = (self.top_y + self.bottom_y) // 2

        picture = cv2.putText(picture, self.text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2)

        return picture

    def get_top_x(self):
        return self.top_left[0]

    def get_top_y(self):
        return self.top_left[1]

    def get_bottom_x(self):
        return self.bottom_right[0]

    def get_bottom_y(self):
        return self.bottom_right[1]

    def field_recognizion(self, top_x, bottom_x, top_y, bottom_y, handx, handy):
        return top_x <= handx <= bottom_x and top_y <= handy <= bottom_y



