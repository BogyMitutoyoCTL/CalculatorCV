import cv2

class FeldActions:

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
            # print(konturen)
            index = self.max_kontur(konturen, minimalgröße)
            if index[0] is not None:
                bild_mit_konturen = cv2.drawContours(ausgangsbild2, [konturen[index[0]]], 0, (255, 255, 255), 2)

                if index[1] is not None:
                    bild_mit_konturen_2 = cv2.drawContours(bild_mit_konturen, [konturen[index[1]]], 0, (255, 255, 255), 2)

                    self.bildspeicher.add_bild(bild_mit_konturen_2, self.bildspeicher.KONTUR)
                    self.datenbank.set_konturen([konturen[index[0]], konturen[index[1]]])
                else:
                    self.bildspeicher.add_bild(bild_mit_konturen, self.bildspeicher.KONTUR)
                    self.datenbank.set_konturen([konturen[index[0]], None])


            else:
                self.bildspeicher.add_bild(None, self.bildspeicher.KONTUR)

    def max_kontur(self, konturen, minimalgröße):
        max_area = 0
        index = None
        index2 = None
        for i in range(len(konturen)):
            area = cv2.contourArea(konturen[i])
            if area > max_area:
                max_area = area
                index2 = index
                index = i
        if index2 is not None:
            if index2 < minimalgröße:
                index2 = None
        return [index, index2]

    def kontur_mittelpunkt(self):
        M = cv2.moments(self.datenbank.get_kontur(0))
        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        else:
            center = None, None

        print(center)