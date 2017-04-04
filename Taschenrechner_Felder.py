import cv2

class Feld:

    def __init__(self, rechner, bildspeicher, datenbank):
        self.rechner = rechner
        self.bildspeicher = bildspeicher
        self.datenbank = datenbank

    def rechenterm_anzeigen(self, zahl1, zahl2, rechenzeichen, index):
        bild = self.bildspeicher.get_bild(index)
        ergebnis = self.rechner.rechne(zahl1, zahl2, rechenzeichen)
        string = str(zahl1) + " " + rechenzeichen + " " + str(zahl2) + " " + "=" + "  " + str(ergebnis)
        bild_mit_text = cv2.putText(bild, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 3)
        self.bildspeicher.add_bild_mit_felder(bild_mit_text, index)


    def feld_erkennung(self, feldx1, feldx2, feldy1, feldy2, handx, handy):
        return feldx1 <= handx <= feldx2 and feldy1 <= handy <= feldy2

    def kontur(self):
        ausgangsbild = self.bildspeicher.get_bild(self.bildspeicher.GRAY2)
        ausgangsbild2 = self.bildspeicher.get_bild(self.bildspeicher.BGR2)
        minimalgröße = self.datenbank.size
        _, konturen, _ = cv2.findContours(ausgangsbild, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if konturen is not None:
            print(konturen)
            index = self.max_kontur(konturen)
            bild_mit_konturen = cv2.drawContours(ausgangsbild2, [konturen[index[0]]], 0, (255, 255, 255), 2  )
            bild_mit_konturen = cv2.drawContours(ausgangsbild2, [konturen[index[1]]], 0, (255, 255, 255), 2)
            self.bildspeicher.add_bild(bild_mit_konturen, self.bildspeicher.KONTUR)


    def max_kontur(self, konturen):
        max_area = 0
        index = 0
        index2 = 0
        for i in range(len(konturen)):
            area = cv2.contourArea(konturen[i])
            if area > max_area:
                max_area = area
                index2 = i
                index = index2
        return [index, index2]
