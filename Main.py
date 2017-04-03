import Taschenrechner_Bild
import Bildbearbeitungstools
import Bildspeicher
import Datenbank
import Taschenrechner_Fenster




bildspeicher = Bildspeicher.Bildspeicher()
datenbank = Datenbank.Datenbank()
camera = Taschenrechner_Bild.Picture(bildspeicher)
tools = Bildbearbeitungstools.Bildbearbeitungstools(bildspeicher, datenbank)
fenster = Taschenrechner_Fenster.Window(datenbank)



fenster.create_window("Bilder")
camera.save_picture()
bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.BGR, fenster)
fenster.wait_key()
tools.convert_brg2hsv()
bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.HSV, fenster)
fenster.wait_key()
tools.glove_filter()
bildspeicher.bild_anzeigen(False, "Bilder", bildspeicher.GRAY, fenster)
fenster.wait_key()
