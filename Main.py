from Camera import Camera
import ImageProcessing
from PictureStorage import PictureStorage
import Settings
from Window import Window
import GUI
import Calculator
import Button

picture_storage = PictureStorage()
settings = Settings.Settings()
camera = Camera()
tools = ImageProcessing.ImageProcessing(picture_storage, settings)
window = Window(settings, tools, "Bilder")
rechner = Calculator.Calculator()
felder = GUI.GUI(rechner, picture_storage, settings)
feld = Button.Button(40, 60, 40, 60, picture_storage)


window.create_trackbars()
while True:
    camera_picture = camera.get_picture()
    picture_storage.add_picture(camera_picture, picture_storage.ORIGINAL_FROM_CAMERA_BGR)
    window.show_picture(picture_storage.get_picture(picture_storage.ORIGINAL_FROM_CAMERA_BGR))
    window.wait_key()
    camera_converted_to_hsv = tools.convert_to_hsv(camera_picture)
    picture_storage.add_picture(camera_converted_to_hsv, picture_storage.CAMERA_CONVERTED_HSV)
    window.show_picture(picture_storage.get_picture(picture_storage.CAMERA_CONVERTED_HSV))
    window.wait_key()
    tools.glove_filter()
    window.show_picture(picture_storage.get_picture(picture_storage.GLOVES_BW))
    window.wait_key()
    tools.blur(10)
    blurred_picture = picture_storage.get_picture(picture_storage.GLOVES_BLURRED_BW)
    window.show_picture(blurred_picture)
    window.wait_key()
    tools.color_glove()
    window.show_picture(picture_storage.get_picture(picture_storage.GLOVES_WITH_ORIGINAL_BGR))
    window.wait_key()
    felder.paint_term(3, "/", None, 1)
    window.show_picture(picture_storage.get_picture(picture_storage.ORIGINAL_WITH_FELD))
    window.wait_key()
    hands = tools.get_hands(blurred_picture, settings.minimum_recognition_size_px, 2)
    for hand in hands:
        print(hand.center)
        hand.get_center()
        print(hand.center)
        hand.fingers(blurred_picture)
    window.show_picture(tools.draw_hands(hands, blurred_picture))
    window.wait_key()
