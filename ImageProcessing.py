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

    def glove_filter(self, hsv_image):
        lowerhsv = (self.settings.lower_h, self.settings.lower_s, self.settings.lower_v)
        upperhsv = (self.settings.upper_h, self.settings.upper_s, self.settings.upper_v)
        gloves_bw_image = cv2.inRange(hsv_image, lowerhsv, upperhsv)

        return gloves_bw_image

    def blur(self, blur_size, gloves_bw_image):
        blurred = cv2.blur(gloves_bw_image, (blur_size, blur_size))
        blurred_bw_image = cv2.inRange(blurred, (self.INCLUSIVE_GRAY), (self.WHITE))

        return blurred_bw_image

    def color_glove(self, bgr_image, blurred_bw_image):
        mask = cv2.bitwise_not(blurred_bw_image)
        color_glove_image = cv2.bitwise_and(bgr_image, self.ALL_CHANNELS, bgr_image, mask)

        return color_glove_image

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
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(picture_with_hands, str(count_fingers), (0, 100), font, 3, (255, 255, 255), 3)
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
