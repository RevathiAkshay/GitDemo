from classtest import calclulator


class childclass1(calclulator):
    z = 200

    def __init__(self):
        calclulator.__init__(self, 2,5)

    def calculation1(self):
        return(self.z + self.num + self.summation())


obj2 = childclass1()
print(obj2.calculation1())i





