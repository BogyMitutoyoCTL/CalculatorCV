class Historie:
    def __init__(self):

        self.Handlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    def ad_Handposition(self, handposition):

        self.Handlist[0:0] = [handposition]
        del self.Handlist[20]
        print(self.Handlist)


test = Historie()
test.ad_Handposition(61)
test.ad_Handposition(54)
test.ad_Handposition(1)
