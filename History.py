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
        for x in range(0, len(self.hand_list)):
            if self.confirm_finger(x) is True:
                number = self.get_number_of_fingers(x)
        return number

    def confirm_finger(self, x) -> bool:
        time_now = self.get_time(x)
        time_old = time_now
        i = x + 1
        while i < len(self.hand_list) and self.get_number_of_fingers(i) == self.get_number_of_fingers(x):
            time_old = self.get_time(i)
            i += 1
        time_difference = time_now - time_old
        return time_difference >= datetime.timedelta(0, 2, 0, 0, 0, 0, 0)

    def confirmed_delete(self, button_generator: ButtonGenerator):
        delete = None
        if self.confirm_button(button_generator.generate_all_buttons()[3]) is True:
            delete = 1
        return delete

    def confirmed_operator(self, button_generator: ButtonGenerator):
        operator = None
        if self.confirm_button(button_generator.generate_all_buttons()[0]) is True:
            operator = "+"
        if self.confirm_button(button_generator.generate_all_buttons()[1]) is True:
            operator = "-"
        if self.confirm_button(button_generator.generate_all_buttons()[2]) is True:
            operator = "*"
        if self.confirm_button(button_generator.generate_all_buttons()[4]) is True:
            operator = "/"
        return operator

    def confirm_button(self, button: Button) -> bool:
        time_now = self.get_time(0)
        time_old = time_now
        i = 0
        while i < len(self.hand_list) and button.contains_point(self.get_center_of_hand(i)[0], self.get_center_of_hand(i)[1]):
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


