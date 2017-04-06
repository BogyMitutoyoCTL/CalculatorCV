class PictureStorage:
    def __init__(self):
        self.pictures = [None, None, None, None, None, None, None, None, None]

        # Constants for picture indexes
        self.ORIGINAL_FROM_CAMERA_BGR = 0
        self.CAMERA_CONVERTED_HSV = 1
        self.GLOVES_BW = 2
        self.GLOVES_BLURRED_BW = 3
        self.GLOVES_WITH_ORIGINAL_BGR = 4
        self.CONTOUR_OF_GLOVES_BGR = 5
        self.CIRCLE_CENTER_BGR = 6
        self.HANDS_BW = 7
        self.ORIGINAL_WITH_FELD = 8

    def add_picture(self, bild, index):
        self.pictures[index] = bild

    def get_picture(self, index):
        return self.pictures[index]
