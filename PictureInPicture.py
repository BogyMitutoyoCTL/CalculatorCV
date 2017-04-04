import cv2


class PictureInPicture:
    def __init__(self):
        pass

    @staticmethod
    def add(large_picture, x, y, small_picture, width, height):
        resized = small_picture
        if len(small_picture) != height or len(small_picture[0]) != height:
            resized = cv2.resize(small_picture, (width, height))
        large_picture[y:y+height, x:x+width] = resized