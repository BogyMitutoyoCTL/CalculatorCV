import datetime

class History:
    def __init__(self):
        self.Handlist = []

    def add_information(self, position_of_hand_x, position_of_hand_y, time, number_of_fingers, operator):

        self.Handlist.insert(0,[position_of_hand_x, position_of_hand_y, time, number_of_fingers, operator])

    def get_position_of_hand_x(self, index):
        return self.Handlist[index][0]

    def get_position_of_hand_y(self, index):
        return self.Handlist[index][1]

    def get_time(self, index):
        return self.Handlist[index][2]

    def get_number_of_fingers(self, index):
        return self.Handlist[index][3]

    def get_operator(self, index):
        return self.Handlist[index][4]

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


test = History()
test.add_information(61, 5, datetime.datetime(2017, 4, 6, 12, 45, 10), 6, None)
test.add_information(54, 6, datetime.datetime(2017, 4, 6, 12, 45, 11), 6, "+")
test.add_information(1, 7, datetime.datetime(2017, 4, 6, 12, 45, 12), 6, "-")
test.add_information(61, 5, datetime.datetime(2017, 4, 6, 12, 45, 13), 5, None)
test.add_information(54, 6, datetime.datetime(2017, 4, 6, 12, 45, 14), 8, "+")
test.add_information(61, 5, datetime.datetime(2017, 4, 6, 12, 45, 19), 5, None)
test.add_information(61, 5, datetime.datetime(2017, 4, 6, 12, 45, 20), 8, None)

print(test.Handlist)
print(test.confirm_fingers())
if __name__ == "__main__":
    print("Please run Main.")
