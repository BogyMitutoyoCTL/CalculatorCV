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

    def glove_filter(self):
        # TODO: ähnlich umbauen wie convert_to_hsv() (Paul)
        lowerhsv = (self.settings.lower_h, self.settings.lower_s, self.settings.lower_v)
        upperhsv = (self.settings.upper_h, self.settings.upper_s, self.settings.upper_v)
        hsv_image = self.picture_storage.get_picture(self.picture_storage.CAMERA_CONVERTED_HSV)
        self.picture_storage.add_picture(cv2.inRange(hsv_image, lowerhsv, upperhsv), self.picture_storage.GLOVES_BW)

    def blur(self, blur_size):
        blurred = cv2.blur(self.picture_storage.get_picture(self.picture_storage.GLOVES_BW), (blur_size, blur_size))
        blurred_bw = cv2.inRange(blurred, (self.INCLUSIVE_GRAY), (self.WHITE))
        self.picture_storage.add_picture(blurred_bw, self.picture_storage.GLOVES_BLURRED_BW)

    def color_glove(self):
        mask = cv2.bitwise_not(self.picture_storage.get_picture(self.picture_storage.GLOVES_BLURRED_BW))
        source = self.picture_storage.get_picture(self.picture_storage.ORIGINAL_FROM_CAMERA_BGR).copy()
        glove_combined = cv2.bitwise_and(source, self.ALL_CHANNELS, source, mask)
        self.picture_storage.add_picture(glove_combined, self. picture_storage.GLOVES_WITH_ORIGINAL_BGR)

