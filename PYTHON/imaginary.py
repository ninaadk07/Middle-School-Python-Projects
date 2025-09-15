class imaginary:
    def __init__(self,r=0,i=0):
        self.r = r
        self.i = i
    def printout(self):
        print("{0}+{1}i".format(self.r,self.i))
        
c1 = imaginary(10,5)   
c1.printout()


