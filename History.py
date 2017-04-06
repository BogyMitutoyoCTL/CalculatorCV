class History:
    def __init__(self):

        self.Handlist = []
        i = 0
        while i <= 20:
            self.Handlist.append([None, None, None, None, None])
            i = i + 1

    def add_position_of_hand(self, position_of_hand_x, position_of_hand_y, time, number_of_fingers, operator):

        self.Handlist[0:0] = [position_of_hand_x, position_of_hand_y, time, number_of_fingers, operator]
        del self.Handlist[20]
        print(self.Handlist)


test = History()
test.add_position_of_hand(61, 5, 1, 8, None)
test.add_position_of_hand(54, 6, 2, 8, "+")
test.add_position_of_hand(1, 7, 3, 3, "-")
if __name__ == "__main__":
    print("Please run Main.")