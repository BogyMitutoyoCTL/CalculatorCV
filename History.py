<<<<<<< HEAD
class Historie:
=======
class History:
>>>>>>> origin/master
    def __init__(self):

        self.Handlist = []
        i = 0
<<<<<<< HEAD
        while i <=20:
            self.Handlist.append([None, None])
            i = i + 1



    def ad_Handposition(self, handposition, uhrzeit):

        self.Handlist[0:0][0:0] = [handposition]
        self.Handlist[0:1][0:0] = [uhrzeit]
=======
        while i <= 20:
            self.Handlist.append([None, None])
            i = i + 1

    def add_position_of_hand(self, position_of_hand, time):

        self.Handlist[0:0][0:0] = [position_of_hand]
        self.Handlist[0:1][0:0] = [time]
>>>>>>> origin/master
        del self.Handlist[20]
        print(self.Handlist)


<<<<<<< HEAD
test = Historie()
test.ad_Handposition(61)
test.ad_Handposition(54)
test.ad_Handposition(1)
=======
test = History()
test.add_position_of_hand(61)
test.add_position_of_hand(54)
test.add_position_of_hand(1)
>>>>>>> origin/master
