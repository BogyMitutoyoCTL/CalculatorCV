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


