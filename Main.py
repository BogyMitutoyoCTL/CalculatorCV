import Taschenrechner_Bild
import Bildbearbeitungstools
import Bildspeicher
import Datenbank
import Taschenrechner_Fenster
import Taschenrechner_Felder
import Rechner
import Klasse_Feld




bildspeicher = Bildspeicher.Bildspeicher()
datenbank = Datenbank.Datenbank()
camera = Taschenrechner_Bild.Picture(bildspeicher)
tools = Bildbearbeitungstools.Bildbearbeitungstools(bildspeicher, datenbank)
fenster = Taschenrechner_Fenster.Window(datenbank, tools)
rechner = Rechner.Rechner()
felder = Taschenrechner_Felder.FeldActions(rechner, bildspeicher, datenbank)
feld = Klasse_Feld.Feld(40, 60, 40, 60, bildspeicher)


fenster.create_window("Bilder")
fenster.create_Trackbar("Bilder")
while True:
    camera.save_picture()
    bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.BGR, fenster)
    fenster.wait_key()
    tools.convert_brg2hsv()
    bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.HSV, fenster)
    fenster.wait_key()
    tools.glove_filter()
    bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.GRAY, fenster)
    fenster.wait_key()
    tools.blur(10, 10)
    bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.GRAY2, fenster)
    fenster.wait_key()
    tools.color_glove()
    bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.BGR2, fenster)
    fenster.wait_key()
    felder.rechenterm_anzeigen(3, 2, "+", bildspeicher.BGR2)
    bildspeicher.bild_anzeigen(True, "Bilder", bildspeicher.BGR2, fenster)
    fenster.wait_key()
    feld.draw_feld(bildspeicher.BGR)
    bildspeicher.bild_anzeigen(True,"Bilder", bildspeicher.BGR, fenster)
    fenster.wait_key()
    felder.kontur()
    bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.KONTUR, fenster)
    felder.kontur_mittelpunkt()
    fenster.wait_key