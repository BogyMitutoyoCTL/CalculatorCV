from Camera import Camera
import ImageProcessing
from PictureStorage import PictureStorage
import Settings
from Window import Window
import GUI
import Calculator
from Button import Button
from ButtonGenerator import ButtonGenerator
import cv2
import multiprocessing
import KeyListener
from History import History
import pyautogui

class Main:

    def __init__(self):
        self.picture_storage = None
        self.settings = None
        self.camera = None
        self.tools = None
        self.window = None
        self.main_window = None
        self.calculator = None
        self.gui = None
        self.picture_to_show = None
        self.keyboard_input = None
        self.history = None
        self.stage = None
        self.number1 = None
        self.number2 = None
        self.operator = None
        self.buttons = None
        self.delete_history = None

    def start(self, getter):
        self.keyboard_input = getter
        self.picture_to_show = self.keyboard_input.get()
        self.picture_storage = PictureStorage()
        self.settings = Settings.Settings()
        self.camera = Camera()
        self.tools = ImageProcessing.ImageProcessing(self.picture_storage, self.settings)
        self.window = Window(self.settings, "Bilder")
        self.main_window = Window(self.settings, "Taschenrechner")
        self.calculator = Calculator.Calculator()
        self.gui = GUI.GUI(self.picture_storage, self.settings)
        self.history = History()
        self.stage = 0
        self.buttons = ButtonGenerator(self.picture_storage)
        self.delete_history = History()
        self._run()

    def _run(self):
        self.window.create_trackbars()
        while self.picture_to_show != -1:
            if not self.keyboard_input.empty():
                self.picture_to_show = self.keyboard_input.get()

            camera_picture = self.tools.flip(self.camera.get_picture())
            self.picture_storage.add_picture(camera_picture.copy(), self.picture_storage.ORIGINAL_FROM_CAMERA_BGR)
            self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.ORIGINAL_FROM_CAMERA_BGR))
            self.buttons.add_size()

            fields = self.buttons.generate_all_buttons()
            field_picture = camera_picture
            for field in fields:
                field_picture = field.draw_field(field_picture)
                self.picture_storage.add_picture(field_picture, self.picture_storage.GUI_BGR)
                self.window.show_picture(field_picture)

            camera_converted_to_hsv = self.tools.convert_to_hsv(camera_picture)
            self.picture_storage.add_picture(camera_converted_to_hsv, self.picture_storage.CAMERA_CONVERTED_HSV)
            self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.CAMERA_CONVERTED_HSV))

            camera_glove_bw = self.tools.glove_filter(camera_converted_to_hsv)
            self.picture_storage.add_picture(camera_glove_bw, self.picture_storage.GLOVES_BW)
            self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.GLOVES_BW))

            camera_blurred_bw = self.tools.blur(10, camera_glove_bw)
            self.picture_storage.add_picture(camera_blurred_bw, self.picture_storage.GLOVES_BLURRED_BW)
            self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.GLOVES_BLURRED_BW))

            camera_glove_bgr = self.tools.color_glove(camera_picture, camera_blurred_bw)
            self.picture_storage.add_picture(camera_glove_bgr, self.picture_storage.GLOVES_WITH_ORIGINAL_BGR)
            self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.GLOVES_WITH_ORIGINAL_BGR))

            hands = self.tools.get_hands(camera_blurred_bw, self.settings.minimum_recognition_size_px)
            countfingers = 0
            for hand in hands:
                hand.init_center()
                hand_picture = hand.fingers(camera_blurred_bw)
                self.window.show_picture(hand_picture)

                if self.stage == 1:
                    self.history.add_information(hand.center_of_hand, None)
                self.delete_history.add_information(hand.center_of_hand, None)
                text = str(hand.number_of_fingers)
                pic = self.tools.text_in_center_hand(self.picture_storage.get_picture(self.picture_storage.GUI_BGR),
                                                hand.center_of_hand, text)
                self.picture_storage.add_picture(pic, self.picture_storage.GUI_BGR)
                countfingers += hand.number_of_fingers
                picture_hight = len(hand_picture)
                picture_width = len(hand_picture[0])
                display_width, display_hight = pyautogui.size()
                pyautogui.FAILSAFE = False
                pyautogui.moveTo(hand.center_of_hand[0] * (display_width/(0.75 * picture_width)) - 100, hand.center_of_hand[1] * (display_hight/(0.75 * picture_hight)) - 100)

            if len(hands) > 0:
                if self.stage == 0:
                    self.history.add_information(None, countfingers)
                    if self.history.confirmed_finger_number() is not None:
                        self.number1 = countfingers
                        if countfingers == 1:
                            pyautogui.click()
                        elif countfingers == 2:
                            pyautogui.rightClick()
                        self.stage = 0
                        self.history.reset()
                        self.delete_history.reset()

            term = self.calculator.get_term_from_numbers(self.number1, self.operator, self.number2)
            self.gui.paint_term(term)

            hands_picture_bw = self.tools.draw_hands(hands, camera_blurred_bw)
            self.picture_storage.add_picture(hands_picture_bw, self.picture_storage.HANDS_BW)
            hands_picture_bgr = self.tools.draw_hands(hands, self.picture_storage.get_picture(self.picture_storage.GUI_BGR))
            self.picture_storage.add_picture(hands_picture_bgr, self.picture_storage.GUI_BGR)
            #self.window.show_picture(hands_picture_bw)
            #self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.GUI_BGR))

            #self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.GUI_BGR))
            #self.main_window.show_picture(self.picture_storage.get_picture(self.picture_to_show))
            #self.window.wait_key(10)

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    queue.put(6)
    key_listener = KeyListener.KeyListener()
    main_object = Main()
    main_thread = multiprocessing.Process(target=main_object.start, args=(queue,))

    key_thread = multiprocessing.Process(target=key_listener.start, args=(queue,))
    key_thread.start()
    main_thread.start()
    main_thread.join()
    key_thread.join()

