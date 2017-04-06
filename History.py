import datetime
from HistoryData import HistoryData
from Button import Button
from ButtonGenerator import ButtonGenerator


class History:
    def __init__(self):
        self.Handlist = []

    def add_information(self, center_of_hand, number_of_fingers, operator):
        time = datetime.datetime.now()
        history_data = HistoryData(center_of_hand, time, number_of_fingers, operator)
        self.Handlist.insert(0, history_data)

    def get_center_of_hand(self, index):
        return self.Handlist[index].center_of_hand

    def get_time(self, index):
        return self.Handlist[index].time

    def get_number_of_fingers(self, index):
        return self.Handlist[index].number_of_fingers

    def get_operator(self, index):
        return self.Handlist[index].operator

    def confirmed_finger_number(self):
        number = None
        for x in range(0, len(self.Handlist)):
            if self.confirm_finger(x) is True:
                number = self.get_number_of_fingers(x)
        return number

    def confirm_finger(self, x):

        self.get_number_of_fingers(x)
        time_now = self.get_time(x)
        time_old = time_now
        i = x + 1
        while i < len(self.Handlist) and self.get_number_of_fingers(i) == self.get_number_of_fingers(x):
            time_old = self.get_time(i)
            i += 1
        time_difference = time_now - time_old
        return time_difference >= datetime.timedelta(0, 2, 0, 0, 0, 0, 0)

    def confirmed_operator(self, button_generator: ButtonGenerator):
        operator = None
        if self.is_hand_center_in_addition(button_generator.generate_all_buttons()[0]) is True:
            operator = "+"
        if self.is_hand_center_in_subtraction(button_generator.generate_all_buttons()[1]) is True:
            operator = "-"
        if self.is_hand_center_in_multiply(button_generator.generate_all_buttons()[2]) is True:
            operator = "*"
        if self. is_hand_center_in_divide(button_generator.generate_all_buttons()[4]) is True:
            operator = "/"
        return operator

    def is_hand_center_in_addition(self, addition: Button):
        self.get_center_of_hand(0)
        time_now = self.get_time(0)
        time_old = time_now
        i = 0
        while i < len(self.Handlist) and addition.field_recognition(self.get_center_of_hand(i)[0], self.get_center_of_hand(i)[1]):
            time_now = self.get_time(i)
            i += 1
        time_difference = time_now - time_old
        return time_difference >= datetime.timedelta(0, 2, 0, 0, 0, 0, 0)

    def is_hand_center_in_subtraction(self, subtraction: Button):
        self.get_center_of_hand(0)
        time_now = self.get_time(0)
        time_old = time_now
        i = 0
        while i < len(self.Handlist) and subtraction.field_recognizion(self.get_center_of_hand(i)[0], self.get_center_of_hand(i)[1]):
            time_now = self.get_time(i)
            i += 1
        time_difference = time_now - time_old
        return time_difference >= datetime.timedelta(0, 2, 0, 0, 0, 0, 0)

    def is_hand_center_in_multiply(self, multiply: Button):
        self.get_center_of_hand(0)
        time_now = self.get_time(0)
        time_old = time_now
        i = 0
        while i < len(self.Handlist) and multiply.field_recognizion(self.get_center_of_hand(i)[0], self.get_center_of_hand(i)[1]):
            time_now = self.get_time(i)
            i += 1
        time_difference = time_now - time_old
        return time_difference >= datetime.timedelta(0, 2, 0, 0, 0, 0, 0)

    def is_hand_center_in_divide(self, division: Button):
        self.get_center_of_hand(0)
        time_now = self.get_time(0)
        time_old = time_now
        i = 0
        while i < len(self.Handlist) and division.field_recognizion(self.get_center_of_hand(i)[0], self.get_center_of_hand(i)[1]):
            time_now = self.get_time(i)
            i += 1
        time_difference = time_now - time_old
        return time_difference >= datetime.timedelta(0, 2, 0, 0, 0, 0, 0)

test = History()
test.add_information((61, 5), 6, None)
test.add_information((54, 6), 6, "+")
test.add_information((1, 7), 6, "-")
test.add_information((61, 5), 5, None)
test.add_information((54, 6), 8, "+")
test.add_information((61, 5), 5, None)
test.add_information((61, 5), 8, None)

print(test.Handlist)
print(test.confirmed_finger_number())
print(test.get_center_of_hand(0))
if __name__ == "__main__":
    print("Please run Main.")


