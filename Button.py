import cv2
from PictureStorage import PictureStorage
from ButtonGenerator import ButtonGenerator
# TODO: merge with Felder.py (Paul)
class Button:
    def __init__(self, top_x: int, bottom_x:int, top_y : int, bottom_y:int, text, picture_storage: PictureStorage):
        self.top_left = (top_x, top_y)
        self.bottom_right = (bottom_x, bottom_y)
        self.picture = picture_storage
        self.color = (54, 120, 244)
        self.thickness = 5
        self.text = text

    # TODO: move to GUI or delete (Paul)
    def draw_feld(self):
        self.picture = cv2.rectangle(self.picture, self.top_left, self.bottom_right, self.color, self.thickness)

    def put_text(self):

        x =

        self.picture = cv2.putText(self.picture, self.text,(x, y),  cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2)

    def get_top_x(self):
        return self.top_left[0]

    def get_top_y(self):
        return self.top_left[1]

    def get_bottom_x(self):
        return self.bottom_right[0]

    def get_bottom_y(self):
        return self.bottom_right[1]

