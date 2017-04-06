from typing import Tuple
import datetime


class HistoryData:
    def __init__(self, center_of_hand: Tuple[int, int], time: datetime, number_of_fingers: int, operator: str):
        self.center_of_hand = center_of_hand
        self.time = time
        self.number_of_fingers = number_of_fingers
        self.operator = operator
