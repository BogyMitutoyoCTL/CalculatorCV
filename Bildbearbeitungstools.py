import cv2
from PictureStorage import PictureStorage
from Datenbank import Datenbank

class Bildbearbeitungstools():
    def __init__(self, picture_storage : PictureStorage, datenbank : Datenbank):
        self.picture_storage = picture_storage
        self.datenbank = datenbank

    def convert_brg2hsv(self):
        bgr_bild = self.picture_storage.get_picture(self.picture_storage.ORIGINAL_FROM_CAMERA_BGR)
        hsv_bild = cv2.cvtColor(bgr_bild, cv2.COLOR_BGR2HSV)
        self.picture_storage.add_picture(hsv_bild, self.picture_storage.CAMERA_CONVERTED_HSV)

    def glove_filter(self):
        lowerhsv = (self.datenbank.lower_h, self.datenbank.lower_s, self.datenbank.lower_v)
        upperhsv = (self.datenbank.upper_h, self.datenbank.upper_s, self.datenbank.upper_v)
        hsv_bild = self.picture_storage.get_picture(self.picture_storage.CAMERA_CONVERTED_HSV)
        self.picture_storage.add_picture(cv2.inRange(hsv_bild, lowerhsv, upperhsv), self.picture_storage.GLOVES_BW)

    def blur(self, breite, höhe):
        blur_bild = cv2.blur(self.picture_storage.get_picture(self.picture_storage.GLOVES_BW), (breite, höhe))
        blurgray_bild = cv2.inRange(blur_bild, (100), (255))
        self.picture_storage.add_picture(blurgray_bild, self.picture_storage.GLOVES_BLURRED_BW)

    def color_glove(self):
        umgedreht = cv2.bitwise_not(self.picture_storage.get_picture(self.picture_storage.GLOVES_BLURRED_BW))
        source = self.picture_storage.get_picture(self.picture_storage.ORIGINAL_FROM_CAMERA_BGR)
        bgr2_bild = cv2.bitwise_and(source, 1, source, umgedreht)
        self.picture_storage.add_picture(bgr2_bild, self. picture_storage.GLOVES_WITH_ORIGINAL_BGR)

