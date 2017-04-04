import cv2

class FeldActions:

    def __init__(self, rechner, bildspeicher):
        self.rechner = rechner
        self.bildspeicher = bildspeicher

    def rechenterm_anzeigen(self, zahl1, zahl2, rechenzeichen, index):
        bild = self.bildspeicher.get_bild(index)
        ergebnis = self.rechner.rechne(zahl1, zahl2, rechenzeichen)
        string = str(zahl1) + " " + rechenzeichen + " " + str(zahl2) + " " + "=" + "  " + str(ergebnis)
        bild_mit_text = cv2.putText(bild, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 3)
        self.bildspeicher.add_bild_mit_fenster(bild_mit_text, index)

    def feld_erkennung(self, feldx1, feldx2, feldy1, feldy2, handx, handy):
        return feldx1 <= handx <= feldx2 and feldy1 <= handy <= feldy2