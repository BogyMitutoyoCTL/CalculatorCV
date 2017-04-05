import cv2
import numpy


class Hand:
    def __init__(self, count_fingers=None, center=None, big_radius=None, small_radius=None, contour=None, area=None):
        self.count_fingers = count_fingers
        self.center = center
        self.big_radius = big_radius
        self.small_radius = small_radius
        self.contour = contour
        self.area = area

    def count_fingers(self, picture_blurred_bw):
        self.set_radius()
        radius = self.get_small_radius()

        if radius is not None:
            picture_with_circles = cv2.circle(picture_blurred_bw, self.center, radius, (0, 0, 0), -1)
            black_image = numpy.zeros(picture_blurred_bw.shape())
            cv2.circle(black_image, self.center, self.big_radius, (255, 255, 255), -1)
        else:
            picture_with_circles = picture_blurred_bw

        _, contours, _ = cv2.findContours(picture_with_circles, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        count = len(contours) - 1
        if self.center == (0, 0):
            count += 1
        self.count_fingers = count

        return picture_with_circles

    def set_radius(self):
        if self.big_radius is None:
            if self.contour is not None:
                (_, _), radius1 = cv2.minEnclosingCircle(self.contour)
                self.big_radius = int(radius1)
            else:
                self.big_radius = 0
            self.small_radius = int(self.big_radius)

    def get_big_radius(self, ):
        return self.big_radius

    def get_small_radius(self, ):
        return self.small_radius

    def get_center(self):
        M = cv2.moments(self.contour)
        if M["m00"] != 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        else:
            center = (0, 0)

        self.center = center
