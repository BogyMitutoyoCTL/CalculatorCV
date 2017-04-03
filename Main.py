import Taschenrechner_Bild
import Bildbearbeitungstools
import Bildspeicher
import Datenbank
import Taschenrechner_Fenster
import Taschenrechner_Felder
import Rechner




bildspeicher = Bildspeicher.Bildspeicher()
datenbank = Datenbank.Datenbank()
camera = Taschenrechner_Bild.Picture(bildspeicher)
tools = Bildbearbeitungstools.Bildbearbeitungstools(bildspeicher, datenbank)
fenster = Taschenrechner_Fenster.Window(datenbank, tools)
rechner = Rechner.Rechner()
felder = Taschenrechner_Felder.Feld(rechner, bildspeicher)



fenster.create_window("Bilder")
camera.save_picture()
bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.BGR, fenster)
fenster.wait_key()
tools.convert_brg2hsv()
bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.HSV, fenster)
fenster.create_Trackbar("Bilder")
fenster.wait_key()
tools.glove_filter()
bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.GRAY, fenster)
fenster.wait_key()
felder.rechenterm_anzeigen(3, 2, "+", bildspeicher.GRAY)
bildspeicher.bild_anzeigen(True, "Bilder", bildspeicher.GRAY, fenster)
fenster.wait_key()
