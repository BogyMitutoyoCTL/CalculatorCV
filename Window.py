import cv2
import Settings

class Window:

    def __init__(self, datenbank, bildbearbeitungstools, window_name):
        self.datenbank = datenbank
        self.bildbearbeitung = bildbearbeitungstools
        self.window_name = window_name
        cv2.namedWindow(window_name)
        self.image_width_px = 1080

    def show_picture(self, picture):
        cv2.imshow(self.window_name, picture)
        # TODO: hack
        self.image_width_px = len(picture[0])

    def wait_key(self, time):
        cv2.waitKey(time) & 0xFF

    def create_trackbars(self):
        cv2.createTrackbar("lower_h", self.window_name, 40, 180, self.lower_h_changed)
        cv2.createTrackbar("upper_h", self.window_name, 69, 180, self.upper_h_changed)
        cv2.createTrackbar("lower_s", self.window_name, 108, 255, self.lower_s_changed)
        cv2.createTrackbar("upper_s", self.window_name, 255, 255, self.upper_s_changed)
        cv2.createTrackbar("lower_v", self.window_name, 32, 255, self.lower_v_changed)
        cv2.createTrackbar("upper_v", self.window_name, 190, 255, self.upper_v_changed)
        cv2.createTrackbar("minimum_recognition_size", self.window_name, 10, 100, self.size_changed)

    def lower_h_changed(self, hue):
        self.datenbank.change_lower_h(hue)
        self.bildbearbeitung.glove_filter()

    def upper_h_changed(self, hue):
        self.datenbank.change_upper_h(hue)
        self.bildbearbeitung.glove_filter()

    def lower_s_changed(self, saturation):
        self.datenbank.change_lower_s(saturation)
        self.bildbearbeitung.glove_filter()

    def upper_s_changed(self, saturation):
        self.datenbank.change_upper_s(saturation)
        self.bildbearbeitung.glove_filter()

    def lower_v_changed(self, value):
        self.datenbank.change_lower_v(value)
        self.bildbearbeitung.glove_filter()

    def upper_v_changed(self, value):
        self.datenbank.change_upper_v(value)
        self.bildbearbeitung.glove_filter()

    def size_changed(self, minimum_recognition_size_percent):
        size_in_px = self.image_width_px * minimum_recognition_size_percent / 100
        self.datenbank.change_size(int(size_in_px))
