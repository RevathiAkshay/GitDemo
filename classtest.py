
## declaring the class
class calclulator:
    num  = 100    ## class variables

#declaring a constructer
    ##declaring instance variables
    def __init__(self, a, b):
        self.num1 =  a
        self.num2 =  b
        print("called automatically")


#declaring the method
    def getdata(self):
        print("Start executions")

    def summation(self):
        return self.num1 + self.num2 + self.num


##caliing the class by creating the object for class


obj = calclulator(2,3)
obj.getdata()
print(obj.summation())
