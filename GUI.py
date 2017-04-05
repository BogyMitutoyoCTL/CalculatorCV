import cv2
from PictureStorage import PictureStorage
from Settings import Settings

class GUI:

    def __init__(self, calculator, picture_storage : PictureStorage, settings : Settings):
        self.calculator = calculator
        self.picture_storage = picture_storage
        self.settings = settings

    def paint_term(self, number1, operator=None, number2=None):
        image = self.picture_storage.get_picture(self.picture_storage.ORIGINAL_FROM_CAMERA_BGR).copy()

        if number2 is None and operator is None:
            string = str(number1)
            image_with_text = cv2.putText(image, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)

        if number2 is None and operator is not None:
            string = str(number1) + " " + operator
            image_with_text = cv2.putText(image, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)

        if number2 is not None and operator is not None:
            result = self.calculator.calculate(number1, number2, operator)
            string = str(number1) + " " + operator + " " + str(number2) + " " + "=" + "  " + str(result)
            image_with_text = cv2.putText(image, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
            self.picture_storage.add_picture(image_with_text, self.picture_storage.ORIGINAL_WITH_FELD)

 # TODO: move to ImageProcessing
    def kontur(self):
        ausgangsbild = self.picture_storage.get_picture(self.picture_storage.GLOVES_BLURRED_BW)
        ausgangsbild2 = self.picture_storage.get_picture(self.picture_storage.GLOVES_WITH_ORIGINAL_BGR)
        minimalgröße = self.settings.minimum_recognition_size_px
        _, konturen, _ = cv2.findContours(ausgangsbild, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if konturen is not None:
            # print(konturen)
            index = self.get_indexes_of_the_two_largest_contours(konturen, minimalgröße)
            if index[0] is not None:
                bild_mit_konturen = cv2.drawContours(ausgangsbild2, [konturen[index[0]]], 0, (255, 255, 255), 2)

                if index[1] is not None:
                    bild_mit_konturen_2 = cv2.drawContours(bild_mit_konturen, [konturen[index[1]]], 0, (255, 255, 255), 2)

                    self.picture_storage.add_picture(bild_mit_konturen_2, self.picture_storage.CONTOUR_OF_GLOVES_BGR)
                    self.settings.set_konturen([konturen[index[0]], konturen[index[1]]])
                else:
                    self.picture_storage.add_picture(bild_mit_konturen, self.picture_storage.CONTOUR_OF_GLOVES_BGR)
                    self.settings.set_konturen([konturen[index[0]], None])


            else:
                self.picture_storage.add_picture(ausgangsbild2, self.picture_storage.CONTOUR_OF_GLOVES_BGR)

    def get_indexes_of_the_two_largest_contours(self, konturen, minimal_size_in_pixel):
        # TODO: areas merken (alle + index dazu) (Arthur)
        # TODO: sortiere die Liste
        # TODO: nimm die Top X
        max_area = 0
        index = None
        index2 = None
        for i in range(len(konturen)):
            area = cv2.contourArea(konturen[i])
            if area < minimal_size_in_pixel:
                continue
            if area >= max_area:
                max_area = area
                index2 = index
                index = i
        return [index, index2]

    # TODO: move to Hand class
    def kontur_mittelpunkt(self):
        M = cv2.moments(self.settings.get_kontur(0))
        if M["m00"] != 0:
            center1 = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        else:
            center1 = (0, 0)

        M = cv2.moments(self.settings.get_kontur(1))
        if M["m00"] != 0:
            center2 = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        else:
            center2 = (0, 0)

        self.settings.set_center1(center1)
        self.settings.set_center2(center2)

        #print(center1, center2)

        # kreis_bild = cv2.circle(self.bildspeicher.get_bild(self.bildspeicher.BGR2), center1, 50, (255, 255, 255))
        # self.bildspeicher.add_bild(kreis_bild, self.bildspeicher.MITTE)

        # kreis_bild = cv2.circle(self.bildspeicher.get_bild(self.bildspeicher.BGR2), center2, 50, (255, 255, 255))
        # self.bildspeicher.add_bild(kreis_bild, self.bildspeicher.MITTE)

    # TODO: move to Hand class
    def count_fingers(self):
        mitte1 = self.settings.get_center1()
        mitte2 = self.settings.get_center2()
        ausgangsbild = self.picture_storage.get_picture(self.picture_storage.GLOVES_BLURRED_BW)
        self.settings.set_radius()
        radius = self.settings.get_radius()


        if radius is not None:
            bild1 = cv2.circle(ausgangsbild, mitte1, radius, (0, 0, 0), -1)
            bild2 = cv2.circle(bild1, mitte2, radius, (0, 0, 0), -1)
        else:
            bild2 = ausgangsbild

        self.picture_storage.add_picture(bild2, self.picture_storage.CIRCLES_ON_GLOVES_BW)

        _, konturen, _ = cv2.findContours(ausgangsbild, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        anzahl = len(konturen) -2
        if mitte1 == (0, 0):
            anzahl += 1
        if mitte2 == (0, 0):
            anzahl += 1
        self.settings.finger_count = anzahl
