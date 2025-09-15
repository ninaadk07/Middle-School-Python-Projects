a=int(input("Enter length : "))
b=int(input("Enter width : "))

class area:

    def __init__(self,l=0,w=0):
        self.l = l
        self.w = w
    def printout(self):
        print(self.l*self.w)
        print(2*(self.l+self.w))
    

x1 = area(a,b)
x1.printout()
