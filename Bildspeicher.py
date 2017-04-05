class Bildspeicher():
    def __init__(self):
        self.bilder = [0, 0, 0, 0, 0, 0, 0, 0]
        self.bilder_mit_feldern = [0, 0, 0, 0, 0, 0, 0, 0]
        self.BGR = 0
        self.HSV = 1
        self.GRAY = 2
        self.BGR2 = 3
        self.KONTUR = 4
        self.GRAY2 = 5
        self.CIRCLES = 6
        self.MITTE = 7

    def add_bild(self, bild, index):
        self.bilder[index] = bild

    def get_bild(self, index):
        return self.bilder[index]

    def add_bild_mit_felder(self, bild_mit_feldern, index):
        self.bilder_mit_feldern[index] = bild_mit_feldern

    def get_bild_mit_felder(self, index):
        return self.bilder_mit_feldern[index]

    def bild_anzeigen(self, felder_ja_nein, index, window):
        if felder_ja_nein is True:
            bild = self.get_bild_mit_felder(index)
        else:
            bild = self.get_bild(index)

        window.show_picture(bild)


