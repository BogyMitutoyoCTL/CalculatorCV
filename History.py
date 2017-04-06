import datetime


class History:
    def __init__(self):
        self.Handlist = []
        self.time = None

    def add_information(self, center_of_hand, number_of_fingers, operator):
        self.time = datetime.datetime.now()
        self.Handlist.insert(0, [center_of_hand, self.time, number_of_fingers, operator])

    def get_center_of_hand(self, index):
        return self.Handlist[index][0]

    def get_time(self, index):
        return self.Handlist[index][1]

    def get_number_of_fingers(self, index):
        return self.Handlist[index][2]

    def get_operator(self, index):
        return self.Handlist[index][3]

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
test.add_information((61, 5), 6, None)
test.add_information((54, 6), 6, "+")
test.add_information((1, 7), 6, "-")
test.add_information((61, 5), 5, None)
test.add_information((54, 6), 8, "+")
test.add_information((61, 5), 5, None)
test.add_information((61, 5), 8, None)

print(test.Handlist)
print(test.confirmed_finger_number())
if __name__ == "__main__":
    print("Please run Main.")
