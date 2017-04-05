import cv2
from PictureStorage import PictureStorage

# TODO: merge with Felder.py
class Button:
    def __init__(self, top_x: int, bottom_x:int, top_y : int, bottom_y:int, picture_storage: PictureStorage):
        self.top_left = (top_x, top_y)
        self.bottom_right = (bottom_x, bottom_y)
        self.picture_storage = picture_storage
        self.color = (255, 255, 255)

    # TODO: move to GUI or delete (Paul)
    def draw_feld(self, index):
        bild_mit_feld = cv2.rectangle(self.picture_storage.get_picture(index), self.top_left, self.bottom_right, self.color)
        self.picture_storage.add_picture_mit_felder(bild_mit_feld, index)

    def get_top_x(self):
        return self.top_left[0]

    def get_top_y(self):
        return self.top_left[1]

    def get_bottom_x(self):
        return self.bottom_right[0]

    def get_bottom_y(self):
        return self.bottom_right[1]

