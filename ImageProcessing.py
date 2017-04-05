import cv2
from PictureStorage import PictureStorage
from Settings import Settings


class ImageProcessing():
    def __init__(self, picture_storage : PictureStorage, settings : Settings):
        self.picture_storage = picture_storage
        self.settings = settings
        self.INCLUSIVE_GRAY = 100
        self.WHITE = 255
        self.ALL_CHANNELS = 1

    def convert_to_hsv(self, bgr_image):
        hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

        return hsv_image

    def glove_filter(self, hsv_image):
        lowerhsv = (self.settings.lower_h, self.settings.lower_s, self.settings.lower_v)
        upperhsv = (self.settings.upper_h, self.settings.upper_s, self.settings.upper_v)
        gloves_bw_image = cv2.inRange(hsv_image, lowerhsv, upperhsv)

        return gloves_bw_image

    def blur(self, blur_size, gloves_bw_image):
        blurred = cv2.blur(gloves_bw_image, (blur_size, blur_size))
        blurred_bw_image = cv2.inRange(blurred, (self.INCLUSIVE_GRAY), (self.WHITE))

        return blurred_bw_image

    def color_glove(self, bgr_image, blurred_bw_image):
        mask = cv2.bitwise_not(blurred_bw_image)
        color_glove_image = cv2.bitwise_and(bgr_image, self.ALL_CHANNELS, bgr_image, mask)

        return color_glove_image

