import cv2
import numpy


class Hand:
    def __init__(self, number_of_fingers=None, center_of_hand=None, big_radius=None, small_radius=None, contour=None, area=None):
        self.number_of_fingers = number_of_fingers
        self.center_of_hand = center_of_hand
        self.big_radius = big_radius
        self.small_radius = small_radius
        self.contour = contour
        self.area = area
        self.finger_contours = None

    def fingers(self, picture_blurred_bw):
        self.set_radius()
        small_radius = self.get_small_radius()
        picture_with_circles = picture_blurred_bw.copy()
        if small_radius is not None:
            size = picture_blurred_bw.shape
            black_image = self.generate_black_image(size)
            self.cut_picture_on_mask(black_image, picture_with_circles)
            self.draw_black_circle_on_white_picture(picture_with_circles, small_radius)

        contours = self.get_finger_contours(picture_with_circles)
        self.count_finger_contours(contours)

        return picture_with_circles

    def count_finger_contours(self, contours):
        number = len(contours) - 1
        self.number_of_fingers = number

    def get_finger_contours(self, picture_with_circles):
        _, contours, _ = cv2.findContours(picture_with_circles, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.finger_contours = contours
        return contours

    def draw_black_circle_on_white_picture(self, picture_with_circles, small_radius):
        cv2.circle(picture_with_circles, self.center_of_hand, small_radius, (0, 0, 0), -1)

    def cut_picture_on_mask(self, black_image, picture_with_circles):
        cv2.bitwise_and(picture_with_circles, 0, picture_with_circles, black_image)

    def generate_black_image(self, size):
        black_image = numpy.zeros((size[0], size[1], 1), numpy.uint8)
        cv2.circle(black_image, self.center_of_hand, self.big_radius, (255, 255, 255), -1)
        cv2.bitwise_not(black_image, black_image)
        return black_image

    def set_radius(self):
        if self.big_radius is None:
            if self.contour is not None:
                (_, _), radius1 = cv2.minEnclosingCircle(self.contour)
                self.big_radius = int(radius1)
            else:
                self.big_radius = 0
            self.small_radius = int(0.7 * self.big_radius)

    def get_big_radius(self):
        return self.big_radius

    def get_small_radius(self):
        return self.small_radius

    def init_center(self):
        M = cv2.moments(self.contour)
        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        else:
            center = (0, 0)

        self.center_of_hand = center
