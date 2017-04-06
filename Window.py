import cv2
import Settings


class Window:
    def __init__(self, settings: Settings, window_name):
        self.settings = settings
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
        cv2.createTrackbar("lower_h", self.window_name, 40, 180, self.settings.change_lower_h)
        cv2.createTrackbar("upper_h", self.window_name, 69, 180, self.settings.change_upper_h)
        cv2.createTrackbar("lower_s", self.window_name, 108, 255, self.settings.change_lower_s)
        cv2.createTrackbar("upper_s", self.window_name, 255, 255, self.settings.change_upper_s)
        cv2.createTrackbar("lower_v", self.window_name, 32, 255, self.settings.change_lower_v)
        cv2.createTrackbar("upper_v", self.window_name, 190, 255, self.settings.change_upper_v)
        cv2.createTrackbar("minimum_recognition_size", self.window_name, 10, 100, self.size_changed_percent)

    def size_changed_percent(self, minimum_recognition_size_percent):
        size_in_px = self.image_width_px * minimum_recognition_size_percent / 100
        self.settings.change_recognition_size(int(size_in_px))
