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
        self.gui = GUI.GUI(self.calculator, self.picture_storage, self.settings)
        self.history = History()
        self.stage = 0
        self.buttons = ButtonGenerator(self.picture_storage)
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

            # window.wait_key()

            camera_converted_to_hsv = self.tools.convert_to_hsv(camera_picture)
            self.picture_storage.add_picture(camera_converted_to_hsv, self.picture_storage.CAMERA_CONVERTED_HSV)
            self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.CAMERA_CONVERTED_HSV))
            # window.wait_key()

            camera_glove_bw = self.tools.glove_filter(camera_converted_to_hsv)
            self.picture_storage.add_picture(camera_glove_bw, self.picture_storage.GLOVES_BW)
            self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.GLOVES_BW))
            # window.wait_key()

            camera_blurred_bw = self.tools.blur(10, camera_glove_bw)
            self.picture_storage.add_picture(camera_blurred_bw, self.picture_storage.GLOVES_BLURRED_BW)
            self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.GLOVES_BLURRED_BW))
            # window.wait_key()

            camera_glove_bgr = self.tools.color_glove(camera_picture, camera_blurred_bw)
            self.picture_storage.add_picture(camera_glove_bgr, self.picture_storage.GLOVES_WITH_ORIGINAL_BGR)
            self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.GLOVES_WITH_ORIGINAL_BGR))
            # window.wait_key()

            # self.gui.paint_term(3, "+", 5)

            #self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.GUI_BGR))
            #self.window.wait_key(0)
            hands = self.tools.get_hands(camera_blurred_bw, self.settings.minimum_recognition_size_px, 2)
            countfingers = 0
            for hand in hands:
                hand.get_center()
                hand_picture = hand.fingers(camera_blurred_bw)
                self.window.show_picture(hand_picture)
                # window.wait_key()
                if self.stage == 1:
                    self.history.add_information(hand.center_of_hand, None, None)

                text = str(hand.number_of_fingers)
                pic = self.tools.text_in_center_hand(self.picture_storage.get_picture(self.picture_storage.GUI_BGR),
                                                hand.center_of_hand, text)
                self.picture_storage.add_picture(pic, self.picture_storage.GUI_BGR)
                countfingers += hand.number_of_fingers

            if self.stage == 0:
                self.history.add_information(None, countfingers, None)
                self.number1 = countfingers
                self.gui.paint_term(self.number1)
                if self.history.confirmed_finger_number() is not None:
                    self.stage = 2
                    self.history.reset()
                    self.operator = '+'
                    jump = True
                    print(jump)

            if self.stage == 1 and jump is False:
                self.gui.paint_term(self.number1)
                confirmed_operator = self.history.confirmed_operator(self.buttons)
                print(confirmed_operator)
                if confirmed_operator is not None:
                    self.operator = confirmed_operator
                    self.gui.paint_term(self.number1, self.operator)
                    self.stage = 2
                    self.history.reset()
            jump = False

            if self.stage == 2:
                self.history.add_information(None, countfingers, None)
                self.number2 = countfingers
                self.gui.paint_term(self.number1, self.operator, self.number2)
                if self.history.confirmed_finger_number() is not None:
                    self.stage = 0
                    self.history.reset()

            hands_picture_bw = self.tools.draw_hands(hands, camera_blurred_bw)
            self.picture_storage.add_picture(hands_picture_bw, self.picture_storage.HANDS_BW)
            hands_picture_bgr = self.tools.draw_hands(hands, self.picture_storage.get_picture(self.picture_storage.GUI_BGR))
            self.picture_storage.add_picture(hands_picture_bgr, self.picture_storage.GUI_BGR)
            self.window.show_picture(hands_picture_bw)
            # window.wait_key()
            self.window.show_picture(self.picture_storage.get_picture(self.picture_storage.GUI_BGR))
            # window.wait_key()



            self.window.show_picture(self.picture_storage.get_picture(self.picture_to_show))
            self.main_window.show_picture(self.picture_storage.get_picture(self.picture_storage.GUI_BGR))
            self.window.wait_key(10)

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

