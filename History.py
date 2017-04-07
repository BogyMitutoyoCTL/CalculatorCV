import datetime
from HistoryData import HistoryData
from Button import Button
from ButtonGenerator import ButtonGenerator
from typing import Tuple


class History:
    def __init__(self):
        self.hand_list = []

    def add_information(self, center_of_hand, number_of_fingers: int, operator) -> None:
        time = datetime.datetime.now()
        history_data = HistoryData(center_of_hand, time, number_of_fingers, operator)
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
            if self.confirm_fingers_from_point_in_past(point_in_history) is True:
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
        if self.confirm_button(button_generator.generate_all_buttons()[3]) is True:
            delete = True
        return delete

    def confirmed_operator(self, button_generator: ButtonGenerator):
        operator = None
        for point_in_history in range(len(self.hand_list)):
            if self.confirm_button_from_point_in_past(button_generator.generate_all_buttons()[0], point_in_history) is True:
                operator = "+"
            if self.confirm_button_from_point_in_past(button_generator.generate_all_buttons()[1], point_in_history) is True:
                operator = "-"
            if self.confirm_button_from_point_in_past(button_generator.generate_all_buttons()[2], point_in_history) is True:
                operator = "*"
            if self.confirm_button_from_point_in_past(button_generator.generate_all_buttons()[4], point_in_history) is True:
                operator = "/"
        return operator

    def confirm_button_from_point_in_past(self, button: Button, x) -> bool:
        time_now = self.get_time(x)
        time_old = time_now
        i = x + 1
        while i < len(self.hand_list) and button.contains_point(self.get_center_of_hand(i)) is True and button.contains_point(self.get_center_of_hand(x))is True:
            time_now = self.get_time(i)
            i += 1
        time_difference = time_now - time_old
        return time_difference >= datetime.timedelta(0, 3, 0, 0, 0, 0, 0)

    def reset(self):
        self.hand_list = []

test = History()
test.add_information((61, 5), 6, None)
test.add_information((54, 6), 6, "+")
test.add_information((1, 7), 6, "-")
test.add_information((61, 5), 5, None)
test.add_information((54, 6), 8, "+")
test.add_information((61, 5), 5, None)
test.add_information((61, 5), 8, None)

print(test.hand_list)
print(test.confirmed_finger_number())
print(test.get_center_of_hand(0))
if __name__ == "__main__":
    print("Please run Main.")


