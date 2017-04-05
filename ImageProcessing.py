import cv2
from PictureStorage import PictureStorage
from Settings import Settings
from Hand import Hand


class ImageProcessing():
    def __init__(self, picture_storage : PictureStorage, settings : Settings):
        self.picture_storage = picture_storage
        self.settings = settings
        self.INCLUSIVE_GRAY = 100
        self.WHITE = 255
        self.ALL_CHANNELS = 1

    def convert_to_hsv(self, bgr_image):
        hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
        return hsv_image

    def glove_filter(self):
        # TODO: ähnlich umbauen wie convert_to_hsv() (Paul)
        lowerhsv = (self.settings.lower_h, self.settings.lower_s, self.settings.lower_v)
        upperhsv = (self.settings.upper_h, self.settings.upper_s, self.settings.upper_v)
        hsv_image = self.picture_storage.get_picture(self.picture_storage.CAMERA_CONVERTED_HSV)
        self.picture_storage.add_picture(cv2.inRange(hsv_image, lowerhsv, upperhsv), self.picture_storage.GLOVES_BW)

    def blur(self, blur_size):
        blurred = cv2.blur(self.picture_storage.get_picture(self.picture_storage.GLOVES_BW), (blur_size, blur_size))
        blurred_bw = cv2.inRange(blurred, (self.INCLUSIVE_GRAY), (self.WHITE))
        self.picture_storage.add_picture(blurred_bw, self.picture_storage.GLOVES_BLURRED_BW)

    def color_glove(self):
        mask = cv2.bitwise_not(self.picture_storage.get_picture(self.picture_storage.GLOVES_BLURRED_BW))
        source = self.picture_storage.get_picture(self.picture_storage.ORIGINAL_FROM_CAMERA_BGR).copy()
        glove_combined = cv2.bitwise_and(source, self.ALL_CHANNELS, source, mask)
        self.picture_storage.add_picture(glove_combined, self. picture_storage.GLOVES_WITH_ORIGINAL_BGR)

    def get_hands(self, start_picture, minimal_size, count):
        hands = []
        _, contours, _ = cv2.findContours(start_picture, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours is not None:
            indexes, areas = self.get_indexes_of_contours_bigger_than_minimal(contours, minimal_size, count)
            for i in range(len(indexes)):
                hands.append(Hand(None, None, None, None, contours[indexes[i]], areas[i]))
        return hands

    def draw_hands(self, hands: [Hand], picture_to_draw_on):
        picture_with_hands = picture_to_draw_on
        count_fingers = 0
        for i in range(len(hands)):
            hand = hands[i]
            picture_with_hands = cv2.drawContours(picture_with_hands, hand.contour, 0, (255, 255, 255), 2)
            picture_with_hands = cv2.circle(picture_with_hands, hand.center, 5, (255, 0, 0), -1)
            count_fingers += hand.count_fingers
        picture_with_hands = cv2.putText(picture_with_hands, count_fingers, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3)
        return picture_with_hands

    def get_indexes_of_contours_bigger_than_minimal(self, contours, minimal_size_in_pixel, count):
        index = []
        areas = []
        for i in range(len(contours)):
            area = cv2.contourArea(contours[i])
            if area < minimal_size_in_pixel:
                continue
            else:
                areas.append(area)
                # TODO: get contours directly
                index.append(i)

        index, areas = self.sort_areas(index, areas)
        index, areas = self.shrink_list_to_count(count, index, areas)
        return index, areas

    # TODO: sort_areas

    def sort_areas(self, index, areas):

        return index, areas

    # TODO: shrink_list_to_count(count, index, areas)

    def shrink_list_to_count(self, count, index, areas):

        return index, areas
