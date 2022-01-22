class calculator:
    num=10

    def __init__(self,a,b):
        print("I am calculator constructor")
        self.firstnumber=a
        self.secondnumber=b

    def getData(self):
        print("I am a method in class")

    def summation(self):
        return self.firstnumber+self.secondnumber


obj= calculator(2,3)

print(obj.summation())

obj.getData()
obj.num
