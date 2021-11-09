from Revision import calculator


class calculator1(calculator):
    num2 = 100


    def __init__(self,e,f):
        self.e = e
        self.f = f
        calculator.__init__(self, 4, 5)

    def sum2(self):
        return self.e + self.f + calculator1.num2 + self.x + self.y


obj2 = calculator1(1,1)
print(obj2.sum2())



