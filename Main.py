from Camera import Camera
import ImageProcessing
from PictureStorage import PictureStorage
import Settings
from Window import Window
import GUI
import Rechner
import Klasse_Feld




picture_storage = PictureStorage()
settings = Settings.Settings()
camera = Camera()
tools = ImageProcessing.ImageProcessing(picture_storage, settings)
window = Window(settings, tools, "Bilder")
rechner = Rechner.Rechner()
felder = GUI.GUI(rechner, picture_storage, settings)
feld = Klasse_Feld.Feld(40, 60, 40, 60, picture_storage)


window.create_trackbars()
while True:
    camera_picture = camera.get_picture()
    picture_storage.add_picture(camera_picture, picture_storage.ORIGINAL_FROM_CAMERA_BGR)
    picture_storage.show_picture(False, picture_storage.ORIGINAL_FROM_CAMERA_BGR, window)
    window.wait_key()
    camera_converted_to_hsv = tools.convert_to_hsv(camera_picture)
    picture_storage.add_picture(camera_converted_to_hsv, picture_storage.CAMERA_CONVERTED_HSV)
    picture_storage.show_picture(False, picture_storage.CAMERA_CONVERTED_HSV, window)
    window.wait_key()
    tools.glove_filter()
    picture_storage.show_picture(False, picture_storage.GLOVES_BW, window)
    window.wait_key()
    tools.blur(10)
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
    print(settings.get_center1(), settings.get_center2())
    felder.finger()
    felder.rechenterm_anzeigen(picture_storage.CIRCLES_ON_GLOVES_BW, settings.finger_count)
    picture_storage.show_picture(True, picture_storage.CIRCLES_ON_GLOVES_BW, window)
    window.wait_key()
    settings.reset()
