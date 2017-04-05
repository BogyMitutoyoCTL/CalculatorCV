from Camera import Camera
import Bildbearbeitungstools
from PictureStorage import PictureStorage
import Datenbank
from Window import Window
import Taschenrechner_Felder
import Rechner
import Klasse_Feld




picture_storage = PictureStorage()
datenbank = Datenbank.Datenbank()
camera = Camera()
tools = Bildbearbeitungstools.Bildbearbeitungstools(picture_storage, datenbank)
window = Window(datenbank, tools, "Bilder")
rechner = Rechner.Rechner()
felder = Taschenrechner_Felder.FeldActions(rechner, picture_storage, datenbank)
feld = Klasse_Feld.Feld(40, 60, 40, 60, picture_storage)


window.create_trackbars()
while True:
    picture_storage.add_picture(camera.get_picture(), picture_storage.ORIGINAL_FROM_CAMERA_BGR)
    picture_storage.show_picture(False, picture_storage.ORIGINAL_FROM_CAMERA_BGR, window)
    window.wait_key()
    tools.convert_brg2hsv()
    picture_storage.show_picture(False, picture_storage.CAMERA_CONVERTED_HSV, window)
    window.wait_key()
    tools.glove_filter()
    picture_storage.show_picture(False, picture_storage.GLOVES_BW, window)
    window.wait_key()
    tools.blur(10, 10)
    picture_storage.show_picture(False, picture_storage.GLOVES_BLURRED_BW, window)
    window.wait_key()
    tools.color_glove()
    picture_storage.show_picture(False, picture_storage.GLOVES_WITH_ORIGINAL_BGR, window)
    window.wait_key()
    felder.rechenterm_anzeigen(picture_storage.GLOVES_WITH_ORIGINAL_BGR, 3, "/", 4)
    picture_storage.show_picture(True, picture_storage.GLOVES_WITH_ORIGINAL_BGR, window)
    window.wait_key()
    felder.kontur()
    picture_storage.show_picture(False, picture_storage.CONTOUR_OF_GLOVES_BGR, window)
    window.wait_key()
    felder.kontur_mittelpunkt()
    print(datenbank.get_center1(), datenbank.get_center2())
    felder.finger()
    felder.rechenterm_anzeigen(picture_storage.CIRCLES_ON_GLOVES_BW, datenbank.anzahl_finger)
    picture_storage.show_picture(True, picture_storage.CIRCLES_ON_GLOVES_BW, window)
    window.wait_key()
    datenbank.reset()
