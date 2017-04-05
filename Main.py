from Camera import Camera
import ImageProcessing
from PictureStorage import PictureStorage
import Settings
from Window import Window
import GUI
import Calculator
from Button import Button
from ButtonGenerator import ButtonGenerator


picture_storage = PictureStorage()
settings = Settings.Settings()
camera = Camera()
tools = ImageProcessing.ImageProcessing(picture_storage, settings)
window = Window(settings, tools, "Bilder")
rechner = Calculator.Calculator()
felder = GUI.GUI(rechner, picture_storage, settings)




window.create_trackbars()
while True:
    camera_picture = camera.get_picture()
    picture_storage.add_picture(camera_picture, picture_storage.ORIGINAL_FROM_CAMERA_BGR)
    window.show_picture(picture_storage.get_picture(picture_storage.ORIGINAL_FROM_CAMERA_BGR))

    TestFenster = ButtonGenerator(picture_storage)
    fields = TestFenster.draw_all_buttons()
    for field in fields:
        field_picture = field.draw_field(camera_picture)


    window.show_picture(field_picture)

    window.wait_key()


    camera_converted_to_hsv = tools.convert_to_hsv(camera_picture)
    picture_storage.add_picture(camera_converted_to_hsv, picture_storage.CAMERA_CONVERTED_HSV)
    window.show_picture(picture_storage.get_picture(picture_storage.CAMERA_CONVERTED_HSV))
    window.wait_key()

    camera_glove_bw = tools.glove_filter(camera_converted_to_hsv)
    picture_storage.add_picture(camera_glove_bw, picture_storage.GLOVES_BW)
    window.show_picture(picture_storage.get_picture(picture_storage.GLOVES_BW))
    window.wait_key()

    camera_blurred_bw = tools.blur(10, camera_glove_bw)
    picture_storage.add_picture(camera_blurred_bw, picture_storage.GLOVES_BLURRED_BW)
    window.show_picture(picture_storage.get_picture(picture_storage.GLOVES_BLURRED_BW))
    window.wait_key()

    camera_glove_bgr = tools.color_glove(camera_picture, camera_blurred_bw)
    picture_storage.add_picture(camera_glove_bgr, picture_storage.GLOVES_WITH_ORIGINAL_BGR)
    window.show_picture(picture_storage.get_picture(picture_storage.GLOVES_WITH_ORIGINAL_BGR))
    window.wait_key()

    felder.paint_term(3, "/", 4)
    window.show_picture(picture_storage.get_picture(picture_storage.ORIGINAL_WITH_FELD))
    window.wait_key()

    felder.kontur()
    window.show_picture(picture_storage.get_picture(picture_storage.CONTOUR_OF_GLOVES_BGR))
    window.wait_key()

    felder.kontur_mittelpunkt()
    print(settings.get_center1(), settings.get_center2())
    felder.count_fingers()
    felder.paint_term(settings.finger_count)
    window.show_picture(picture_storage.get_picture(picture_storage.ORIGINAL_WITH_FELD))
    window.wait_key()
    settings.reset()
