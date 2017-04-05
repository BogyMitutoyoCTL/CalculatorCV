class History:
    def __init__(self):

        self.Handlist = []
        i = 0
        while i <= 20:
            self.Handlist.append([None, None])
            i = i + 1

    def add_position_of_hand(self, position_of_hand, time):

        self.Handlist[0:0][0:0] = [position_of_hand]
        self.Handlist[0:1][0:0] = [time]
        del self.Handlist[20]
        print(self.Handlist)


test = History()
test.add_position_of_hand(61)
test.add_position_of_hand(54)
test.add_position_of_hand(1)
