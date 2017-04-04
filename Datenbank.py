class Datenbank():
    def __init__(self):
        self.upper_h = 98
        self.lower_h = 34
        self.upper_s = 255
        self.lower_s = 125
        self.upper_v = 255
        self.lower_v = 57
        self.size = 0

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

