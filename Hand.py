class Hand():
    def __init__(self):
        self.count_fingers = None
        self.center = (None, None)
        self.big_radius = None
        self.small_radius = int(0.75 * self.big_radius)
        self.contour = None