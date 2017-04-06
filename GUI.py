import cv2
from PictureStorage import PictureStorage
from Settings import Settings


class GUI:

    def __init__(self, calculator, picture_storage: PictureStorage, settings: Settings):
        self.calculator = calculator
        self.picture_storage = picture_storage
        self.settings = settings
        self.section_count = 15
        self.default_button_hight = 2.5

    def paint_term(self, number1, operator=None, number2=None):
        image = self.picture_storage.get_picture(self.picture_storage.ORIGINAL_WITH_FELD).copy()
        hight = len(image)
        width = len(image[0])

        if number2 is None and operator is None:

            x = width / 2
            y = hight / self.section_count * self.default_button_hight

            string = str(number1)
            text_size = cv2.getTextSize(string, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
            text_x = text_size[0][0]
            text_y = text_size[0][1]

            x = x - text_x / 2
            y = y + text_y / 2

            image_with_text = cv2.putText(image, string, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)

        if number2 is None and operator is not None:

            x = width / 2
            y = hight / self.section_count * self.default_button_hight

            string = str(number1) + " " + operator
            text_size = cv2.getTextSize(string, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
            text_x = text_size[0][0]
            text_y = text_size[0][1]

            x = x - text_x / 2
            y = y + text_y / 2

            image_with_text = cv2.putText(image, string, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),2)
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)

        if number2 is not None and operator is not None:
            result = self.calculator.calculate(number1, number2, operator)

            x = width / 2
            y = hight / self.section_count * self.default_button_hight

            string = str(number1) + " " + operator + " " + str(number2) + " " + "=" + " " + str(result)

            text_size = cv2.getTextSize(string, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
            text_x = text_size[0][0]
            text_y = text_size[0][1]

            x = x - text_x / 2
            y = y + text_y / 2

            image_with_text = cv2.putText(image, string, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),
                                          2)
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)