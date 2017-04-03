class Bildspeicher():
    def __init__(self):
        self.bilder = [0,0,0,0,0,0]
        self.bilder_mit_feldern = [0,0,0,0,0,0]

    def add_bild(self, bild, index):
        self.bilder[index] = bild

    def get_bild(self, index):
        return self.bilder[index]

    def add_bild_mit_fenster(self, bild_mit_feldern, index):
        self.bilder_mit_feldern[index] = bild_mit_feldern

    def get_bild_mit_fenster(self, index):
        return self.bilder_mit_feldern[index]


