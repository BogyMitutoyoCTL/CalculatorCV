from Camera import Camera
import ImageProcessing
from PictureStorage import PictureStorage
import Settings
from Window import Window
import GUI
import Calculator
from History import History
from ButtonGenerator import ButtonGenerator
import cv2


picture_storage = PictureStorage()
settings = Settings.Settings()
camera = Camera()
tools = ImageProcessing.ImageProcessing(picture_storage, settings)
window = Window(settings, "Bilder")
main_window = Window(settings, "Taschenrechner")
calculator = Calculator.Calculator()
gui = GUI.GUI(calculator, picture_storage, settings)
key = 6
history = History()

window.create_trackbars()
while True:
    camera_picture = tools.flip(camera.get_picture())
    picture_storage.add_picture(camera_picture, picture_storage.ORIGINAL_FROM_CAMERA_BGR)

    TestFenster = ButtonGenerator(picture_storage)
    fields = TestFenster.generate_all_buttons()
    field_picture = camera_picture
    for field in fields:
        field_picture = field.draw_field(field_picture)
    picture_storage.add_picture(field_picture, picture_storage.ORIGINAL_WITH_FELD)

    camera_converted_to_hsv = tools.convert_to_hsv(camera_picture)
    picture_storage.add_picture(camera_converted_to_hsv, picture_storage.CAMERA_CONVERTED_HSV)

    camera_glove_bw = tools.glove_filter(camera_converted_to_hsv)
    picture_storage.add_picture(camera_glove_bw, picture_storage.GLOVES_BW)

    camera_blurred_bw = tools.blur(10, camera_glove_bw)
    picture_storage.add_picture(camera_blurred_bw, picture_storage.GLOVES_BLURRED_BW)

    camera_glove_bgr = tools.color_glove(camera_picture, camera_blurred_bw)
    picture_storage.add_picture(camera_glove_bgr, picture_storage.GLOVES_WITH_ORIGINAL_BGR)

    gui.paint_term(3, "/", 4)

    hands = tools.get_hands(camera_blurred_bw, settings.minimum_recognition_size_px, 2)
    for hand in hands:
        print(hand.center)
        hand.get_center()
        print(hand.center)
        hand_picture = hand.fingers(camera_blurred_bw)
        window.show_picture(hand_picture)
        history.add_information(hand.center, hand.count_fingers, None)
        text = str(hand.count_fingers)
        pic = tools.text_in_center_hand(picture_storage.get_picture(picture_storage.ORIGINAL_WITH_FELD), hand.center, text)
        window.show_picture(pic)

        window.wait_key(10)
    hands_picture_bw = tools.draw_hands(hands, camera_blurred_bw)
    hands_picture_bgr = tools.draw_hands(hands, field_picture)
    picture_storage.add_picture(hands_picture_bw, picture_storage.HANDS_BW)
    picture_storage.add_picture(hands_picture_bgr, picture_storage.ORIGINAL_WITH_FELD)

    main_window.show_picture(picture_storage.get_picture(picture_storage.ORIGINAL_WITH_FELD))
    window.wait_key(10)

    # TODO: Key ändern


