import cv2
from PictureStorage import PictureStorage
from Settings import Settings
from Hand import Hand
from typing import List
from typing import Tuple

white = (255, 255, 255)

filled = -1

black = (0, 0, 0)


class ImageProcessing:
    def __init__(self, picture_storage: PictureStorage, settings: Settings):
        self.picture_storage = picture_storage
        self.settings = settings
        self.INCLUSIVE_GRAY = 100
        self.WHITE = 255
        self.ALL_CHANNELS = 1
        self.fill = False

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

    def get_hands(self, start_picture, minimal_size: int) -> List[Hand]:
        hands = []
        _, contours, _ = cv2.findContours(start_picture, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours is not None:
            indexes, areas = self.get_indexes_of_contours_bigger_than_minimal(contours, minimal_size)
            for i in range(len(indexes)):
                hands.append(Hand(None, None, None, None, contours[indexes[i]], areas[i], self.settings.factor))
        return hands

    def draw_hands(self, hands: [Hand], picture_to_draw_on):
        picture_with_hands = picture_to_draw_on.copy()
        for i in range(len(hands)):
            hand = hands[i]
            picture_with_hands = cv2.drawContours(picture_with_hands, hand.contour, 0, white)
            picture_with_hands = cv2.circle(picture_with_hands, hand.center_of_hand, 5, black, filled)
            if self.fill:
                picture_with_hands = cv2.circle(picture_with_hands, hand.center_of_hand, hand.small_radius, black, -1)
            else:
                picture_with_hands = cv2.circle(picture_with_hands, hand.center_of_hand, hand.small_radius, black, 2)
            picture_with_hands = cv2.drawContours(picture_with_hands, hand.finger_contours, -1, (255, 255, 255), filled)

        return picture_with_hands

    def get_indexes_of_contours_bigger_than_minimal(self, contours, minimal_size_in_pixel: int) -> Tuple[int, int]:
        index = []
        areas = []
        for i in range(len(contours)):
            area = cv2.contourArea(contours[i])
            if area < minimal_size_in_pixel:
                continue
            else:
                areas.append(area)
                # TODO: get contours directly (optional, looks nicer in code)
                index.append(i)

        index, areas = self.shrink_list_to_count(index, areas)
        return index, areas


    def shrink_list_to_count(self, index, areas):
        return index, areas

    def flip(self, image):
        return cv2.flip(image, 1)

    def text_in_center_hand(self, picture, center, text: str):
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 3, 3)
        width = text_size[0][0]
        hight = text_size[0][1]
        x = center[0]
        x -= width // 2
        y = center[1]
        y += hight // 2

        return cv2.putText(picture, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

