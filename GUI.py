import cv2
from PictureStorage import PictureStorage
from Settings import Settings


class GUI:

    def __init__(self, picture_storage: PictureStorage, settings: Settings):
        self.picture_storage = picture_storage
        self.settings = settings
        self.section_count = 15
        self.default_button_hight = 2.5

    def paint_term(self, string):
        image = self.picture_storage.get_picture(self.picture_storage.GUI_BGR).copy()
        hight = len(image)
        width = len(image[0])
        x = width / 2
        y = hight / self.section_count * self.default_button_hight

        text_size = cv2.getTextSize(string, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        text_x = text_size[0][0]
        text_y = text_size[0][1]

        x -= text_x / 2
        y += text_y / 2

        image_with_text = cv2.putText(image, string, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        self.picture_storage.add_picture(image_with_text, self.picture_storage.GUI_BGR)
