class History:
    def __init__(self, framerate):

        self.Handlist = []
        self.framerate = framerate
        self.i = 0
        while self.i <= 2*framerate:
            self.Handlist.append([None, None, None, None, None])
            self.i += 1

    def add_information(self, position_of_hand_x, position_of_hand_y, time, number_of_fingers, operator):

        self.Handlist[0:0] = [[position_of_hand_x, position_of_hand_y, time, number_of_fingers, operator]]
        del self.Handlist[2*self.framerate+1]
        #print(self.Handlist)

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

    def confirm_fingers(self):
        if self.get_number_of_fingers(2*self.framerate - 1) == self.get_number_of_fingers(0):
            return self.get_number_of_fingers(0)
        else:
            return None


test = History(3)
test.add_information(61, 5, 1, 8, None)
test.add_information(54, 6, 2, 8, "+")
test.add_information(1, 7, 3, 3, "-")
test.add_information(61, 5, 1, 8, None)
test.add_information(54, 6, 2, 8, "+")
test.add_information(61, 5, 1, 8, None)

print(test.Handlist)
print(test.confirm_fingers())
if __name__ == "__main__":
    print("Please run Main.")
