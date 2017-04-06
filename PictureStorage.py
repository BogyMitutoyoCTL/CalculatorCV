class PictureStorage:
    def __init__(self):
        self.pictures = [None, None, None, None, None, None, None, None]

        # Constants for picture indexes
        self.ORIGINAL_FROM_CAMERA_BGR = 0
        self.CAMERA_CONVERTED_HSV = 1
        self.GLOVES_BW = 2
        self.GLOVES_BLURRED_BW = 3
        self.GLOVES_WITH_ORIGINAL_BGR = 4
        self.CONTOUR_OF_GLOVES_BGR = 5
        self.HANDS_BW = 6
        self.ORIGINAL_WITH_FELD = 7

    def add_picture(self, picture, index: int) -> None:
        self.pictures[index] = picture

    def get_picture(self, index: int):
        return self.pictures[index]
