from Camera import Camera
import Bildbearbeitungstools
import Bildspeicher
import Datenbank
from Window import Window
import Taschenrechner_Felder
import Rechner
import Klasse_Feld




bildspeicher = Bildspeicher.Bildspeicher()
datenbank = Datenbank.Datenbank()
camera = Camera(bildspeicher)
tools = Bildbearbeitungstools.Bildbearbeitungstools(bildspeicher, datenbank)
fenster = Window(datenbank, tools, "Bilder")
rechner = Rechner.Rechner()
felder = Taschenrechner_Felder.FeldActions(rechner, bildspeicher, datenbank)
feld = Klasse_Feld.Feld(40, 60, 40, 60, bildspeicher)


fenster.create_trackbars()
while True:
    camera.save_picture()
    bildspeicher.bild_anzeigen(False, bildspeicher.BGR, fenster)
    fenster.wait_key()
    tools.convert_brg2hsv()
    bildspeicher.bild_anzeigen(False,  bildspeicher.HSV, fenster)
    fenster.wait_key()
    tools.glove_filter()
    bildspeicher.bild_anzeigen(False,  bildspeicher.GRAY, fenster)
    fenster.wait_key()
    tools.blur(10, 10)
    bildspeicher.bild_anzeigen(False,  bildspeicher.GRAY2, fenster)
    fenster.wait_key()
    tools.color_glove()
    bildspeicher.bild_anzeigen(False,  bildspeicher.BGR2, fenster)
    fenster.wait_key()
    felder.rechenterm_anzeigen( bildspeicher.BGR2, 3, "/", 4)
    bildspeicher.bild_anzeigen(True,  bildspeicher.BGR2, fenster)
    fenster.wait_key()
    #feld.draw_feld(bildspeicher.BGR)
    #bildspeicher.bild_anzeigen(True, bildspeicher.BGR, fenster)
    fenster.wait_key()
    felder.kontur()
    bildspeicher.bild_anzeigen(False,  bildspeicher.KONTUR, fenster)
    fenster.wait_key()
    felder.kontur_mittelpunkt()
    #bildspeicher.bild_anzeigen(False,  bildspeicher.MITTE, fenster)
    #fenster.wait_key()
    print(datenbank.get_center1(), datenbank.get_center2())
    fenster.wait_key()
    felder.finger()
    felder.rechenterm_anzeigen(bildspeicher.CIRCLES, datenbank.anzahl_finger)
    bildspeicher.bild_anzeigen(True, bildspeicher.CIRCLES, fenster)
    fenster.wait_key()
    datenbank.reset()
