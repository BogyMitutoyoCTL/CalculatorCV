import cv2
from PictureStorage import PictureStorage
from Settings import Settings


class GUI:

    def __init__(self, calculator, picture_storage: PictureStorage, settings: Settings):
        self.calculator = calculator
        self.picture_storage = picture_storage
        self.settings = settings

    def paint_term(self, number1, operator, number2, delete=None):
        image = self.picture_storage.get_picture(self.picture_storage.ORIGINAL_FROM_CAMERA_BGR).copy()

        if number1 is not None and operator is None and number2 is None and delete is not None:
            number1 = None
            image_with_text= image
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)

        if number1 is not None and operator is None and number2 is None and delete is None:
            string = str(number1)
            image_with_text = cv2.putText(image, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)

        if number1 is not None and operator is not None and number2 is None and delete is not None:
            operator = None
            string = str(number1)
            image_with_text = cv2.putText(image, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)

        if number1 is not None and operator is not None and number2 is None and delete is None:
            string = str(number1) + " " + operator
            image_with_text = cv2.putText(image, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)

        if number1 is not None and operator is not None and number2 is not None and delete is not None:
            number2 = None
            string = str(number1) + " " + operator
            image_with_text = cv2.putText(image, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)

        if number1 is not None and operator is not None and number2 is not None and delete is None:
            result = self.calculator.calculate(number1, number2, operator)
            string = str(number1) + " " + operator + " " + str(number2) + " " + "=" + "  " + str(result)
            image_with_text = cv2.putText(image, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)

    # TODO: move to Rectangle
    def feld_erkennung(self, feldx1, feldx2, feldy1, feldy2, handx, handy):
        return feldx1 <= handx <= feldx2 and feldy1 <= handy <= feldy2
