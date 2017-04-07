import datetime
from HistoryData import HistoryData
from Button import Button
from ButtonGenerator import ButtonGenerator
from typing import Tuple


class History:
    def __init__(self):
        self.hand_list = []

    def add_information(self, center_of_hand, number_of_fingers: int) -> None:
        time = datetime.datetime.now()
        history_data = HistoryData(center_of_hand, time, number_of_fingers)
        self.hand_list.insert(0, history_data)

    def get_center_of_hand(self, index) -> Tuple[int, int]:
        return self.hand_list[index].center_of_hand

    def get_time(self, index) -> datetime:
        return self.hand_list[index].time

    def get_number_of_fingers(self, index) -> int:
        return self.hand_list[index].number_of_fingers

    def get_operator(self, index) -> str:
        return self.hand_list[index].operator

    def confirmed_finger_number(self):
        number = None
        for point_in_history in range(len(self.hand_list)):
            if self.confirm_fingers_from_point_in_past(point_in_history):
                number = self.get_number_of_fingers(point_in_history)
        return number

    def confirm_fingers_from_point_in_past(self, x) -> bool:
        time_now = self.get_time(x)
        time_old = time_now
        i = x + 1
        while i < len(self.hand_list) and self.get_number_of_fingers(i) == self.get_number_of_fingers(x):
            time_old = self.get_time(i)
            i += 1
        time_difference = time_now - time_old
        return time_difference >= datetime.timedelta(0, 2, 0, 0, 0, 0, 0)

    def confirmed_delete(self, button_generator: ButtonGenerator) -> bool:
        delete = False
        if self.confirmed_buttons(button_generator.generate_all_buttons()[3]):
            delete = True
        return delete

    def confirmed_operator(self, button_generator: ButtonGenerator):
        operator = None
        
        if self.confirmed_buttons(button_generator.generate_all_buttons()[0]):
            operator = "+"
        if self.confirmed_buttons(button_generator.generate_all_buttons()[1]):
            operator = "-"
        if self.confirmed_buttons(button_generator.generate_all_buttons()[2]):
            operator = "*"
        if self.confirmed_buttons(button_generator.generate_all_buttons()[4]):
            operator = "/"
        return operator

    def confirmed_buttons(self, button: Button):
        for point_in_history in range(len(self.hand_list)):
            if self.confirm_button_from_point_in_past(button, point_in_history):
                return True
        return False
        
    def confirm_button_from_point_in_past(self, button: Button, x) -> bool:
        time_now = self.get_time(x)
        time_old = time_now - datetime.timedelta(0, 3, 0, 0, 0, 0, 0)
        i = x + 1
        in_button_count = 0
        out_of_button_count = 0
        while i < len(self.hand_list) and time_old <= time_now:
            time_now = self.get_time(i)
            if button.contains_point(self.get_center_of_hand(i)):
                in_button_count += 1
            else:
                out_of_button_count += 1
            i += 1
        return (2 * in_button_count) > out_of_button_count

    def reset(self):
        self.hand_list = []

