import cv2

class Datenbank():
    def __init__(self):
        self.upper_h = 69
        self.lower_h = 40
        self.upper_s = 255
        self.lower_s = 108
        self.upper_v = 190
        self.lower_v = 32
        self.size = 0
        self.konturen = [0, 0]
        self.center1 = None
        self.radius = None
        self.anzahl_finger = 0

    def change_lower_h(self, wert):
        self.lower_h = wert

    def change_upper_h(self, wert):
        self.upper_h = wert

    def change_lower_s(self, wert):
        self.lower_s = wert

    def change_upper_s(self, wert):
        self.upper_s = wert

    def change_lower_v(self, wert):
        self.lower_v = wert

    def change_upper_v(self, wert):
        self.upper_v = wert

    def change_size(self, wert):
        self.size = wert

    def set_konturen(self, konturen):
        self.konturen = konturen

    def get_kontur(self, index):
        return self.konturen[index]

    def set_center1(self, center1):
        self.center1 = center1

    def get_center1(self):
        return self.center1

    def set_center2(self, center2):
        self.center2 = center2

    def get_center2(self):
        return self.center2

    def reset(self):
        self.konturen = [0, 0]

    def set_radius(self):
        if self.radius is None:
            kontur1 = self.konturen[0]
            kontur2 = self.konturen[1]
            if kontur1 is not None:
                (_, _), radius1 = cv2.minEnclosingCircle(kontur1)
                radius1 = int(radius1)
            else:
                radius1 = 0
            if kontur2 is not None:
                (_, _), radius2 = cv2.minEnclosingCircle(kontur2)
                radius2 = int(radius2)
            else:
                radius2 = 0
            if radius1 is not None or radius2 is not None:
                if radius1 is None:
                    radius1 = 0
                if radius2 is None:
                    radius2 = 0
                if radius1 < radius2:
                    radius = radius2
                else:
                    radius = radius1
                self.radius = int(0.75 * radius)
            else:
                self.radius = None

    def get_radius(self):
        return self.radius


