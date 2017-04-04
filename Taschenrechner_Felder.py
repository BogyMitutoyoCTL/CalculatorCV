import cv2

class FeldActions:

    def __init__(self, rechner, bildspeicher, datenbank):
        self.rechner = rechner
        self.bildspeicher = bildspeicher
        self.datenbank = datenbank

    def rechenterm_anzeigen(self, index, zahl1, rechenzeichen=None, zahl2=None, reset=None):
        bild = self.bildspeicher.get_bild(index)

        if zahl2 is None and rechenzeichen is None:
            string = str(zahl1)
            bild_mit_text = cv2.putText(bild, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
            self.bildspeicher.add_bild_mit_felder(bild_mit_text, index)

        if zahl2 is None and rechenzeichen is not None:
            string = str(zahl1) + " " + rechenzeichen
            bild_mit_text = cv2.putText(bild, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
            self.bildspeicher.add_bild_mit_felder(bild_mit_text, index)

        if zahl2 is not None and rechenzeichen is not None:
            ergebnis = self.rechner.rechne(zahl1, zahl2, rechenzeichen)
            string = str(zahl1) + " " + rechenzeichen + " " + str(zahl2) + " " + "=" + "  " + str(ergebnis)
            bild_mit_text = cv2.putText(bild, string, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)
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
                self.bildspeicher.add_bild(ausgangsbild2, self.bildspeicher.KONTUR)

    def max_kontur(self, konturen, minimalgröße):
        max_area = 0
        index = None
        index2 = None
        for i in range(len(konturen)):
            area = cv2.contourArea(konturen[i])
            if area >= max_area:
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

        #print(center1, center2)

        # kreis_bild = cv2.circle(self.bildspeicher.get_bild(self.bildspeicher.BGR2), center1, 50, (255, 255, 255))
        # self.bildspeicher.add_bild(kreis_bild, self.bildspeicher.MITTE)

        # kreis_bild = cv2.circle(self.bildspeicher.get_bild(self.bildspeicher.BGR2), center2, 50, (255, 255, 255))
        # self.bildspeicher.add_bild(kreis_bild, self.bildspeicher.MITTE)





    def finger(self):
        mitte1 = self.datenbank.get_center1()
        mitte2 = self.datenbank.get_center2()
        ausgangsbild = self.bildspeicher.get_bild(self.bildspeicher.GRAY2)
        self.datenbank.set_radius()
        radius = self.datenbank.get_radius()


        if radius is not None:
            bild1 = cv2.circle(ausgangsbild, mitte1, radius, (0, 0, 0), -1)
            bild2 = cv2.circle(bild1, mitte2, radius, (0, 0, 0), -1)
        else:
            bild2 = ausgangsbild

        self.bildspeicher.add_bild(bild2, self.bildspeicher.CIRCLES)

        _, konturen, _ = cv2.findContours(ausgangsbild, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        anzahl = len(konturen) -2
        if mitte1 == (0, 0):
            anzahl += 1
        if mitte2 == (0, 0):
            anzahl += 1
        self.datenbank.anzahl_finger = anzahl
