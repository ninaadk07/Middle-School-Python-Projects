print ("1 = addition, 2 = subtraction, 3 = multiplication, 4 = division")
x = int(input("Make choice now : "))
y = int(input("Enter 1st number : "))
z = int(input("Enter 2nd number : "))

class cal:

    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b
    def printout(self):
        if (x==1):
            print(self.a+self.b)
        elif (x==2):
            print(self.a-self.b)
        elif (x==3):
            print(self.a*self.b)
        elif (x==4):
            print(self.a/self.b)0.2f


x1 = cal(y,z)
x1.printout()

    
