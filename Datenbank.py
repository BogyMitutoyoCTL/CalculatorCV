class Datenbank():
    def __init__(self):
        self.upper_h = 76
        self.lower_h = 30
        self.upper_s = 180
        self.lower_s = 70
        self.upper_v = 222
        self.lower_v = 114
        self.size = 0
        self.konturen = [0, 0]

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

