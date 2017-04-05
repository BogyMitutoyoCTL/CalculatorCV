class Historie:
    def __init__(self):

        self.Handlist = []
        i = 0
        while i <=20:
            self.Handlist.append([None, None])
            i = i + 1



    def ad_Handposition(self, handposition, uhrzeit):

        self.Handlist[0:0][0:0] = [handposition]
        self.Handlist[0:1][0:0] = [uhrzeit]
        del self.Handlist[20]
        print(self.Handlist)


test = Historie()
test.ad_Handposition(61)
test.ad_Handposition(54)
test.ad_Handposition(1)
