class Settings:
    def __init__(self):
        self.lower_h = 40
        self.upper_h = 69
        self.lower_s = 108
        self.upper_s = 255
        self.lower_v = 32
        self.upper_v = 190
        self.minimum_recognition_size_px = 0

    def change_lower_h(self, hue: int) -> None:
        self.lower_h = hue

    def change_upper_h(self, hue: int) -> None:
        self.upper_h = hue

    def change_lower_s(self, saturation: int) -> None:
        self.lower_s = saturation

    def change_upper_s(self, saturation: int) -> None:
        self.upper_s = saturation

    def change_lower_v(self, value: int) -> None:
        self.lower_v = value

    def change_upper_v(self, value: int) -> None:
        self.upper_v = value

    def change_recognition_size(self, minimum_size_px: int) -> None:
        self.minimum_recognition_size_px = minimum_size_px
