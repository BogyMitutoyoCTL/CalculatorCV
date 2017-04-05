import cv2

class Hand():
    def __init__(self, count_fingers = None, center = None, big_radius = None, small_radius = None, contour = None, area = None):
        self.count_fingers = count_fingers
        self.center = center
        self.big_radius = big_radius
        self.small_radius = small_radius
        self.contour = contour
        self.area = area





    def count_fingers(self):
        ausgangsbild = self.bildspeicher.get_picture(self.bildspeicher.GLOVES_BLURRED_BW)
        self.set_radius()
        radius = self.get_small_radius()


        if radius is not None:
            bild1 = cv2.circle(ausgangsbild, self.center, radius, (0, 0, 0), -1)
        else:
            bild1 = ausgangsbild

        self.bildspeicher.add_picture(bild1, self.bildspeicher.CIRCLES_ON_GLOVES_BW)

        _, konturen, _ = cv2.findContours(ausgangsbild, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        anzahl = len(konturen) - 1
        if self.center == (0, 0):
            anzahl += 1
        self.datenbank.finger_count = anzahl

    def set_radius(self):
        if self.big_radius is None:
            if self.contour is not None:
                (_, _), radius1 = cv2.minEnclosingCircle(self.contour)
                self.big_radius = int(radius1)
            else:
                self.big_radius = 0
            self.small_radius = int(self.big_radius)

    def get_big_radius(self, ):
        return self.big_radius

    def get_small_radius(self, ):
        return self.small_radius

        # TODO: move to Hand class

    def kontur_mittelpunkt(self):
        M = cv2.moments(self.datenbank.get_kontur(0))
        if M["m00"] != 0:
            center1 = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        else:
            center1 = (0, 0)

        M = cv2.moments(self.datenbank.get_kontur(1))
        if M["m00"] != 0:
            center2 = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        else:
            center2 = (0, 0)

        self.datenbank.set_center1(center1)
        self.datenbank.set_center2(center2)


