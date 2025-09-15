"""a = int(input("Enter upper limit : "))
def factorial(y):
    if (y>=1):    
        return(y * factorial(y-1))
       
    
    else:
        return(1) 
             
               
y = a
"""

a = int(input("Enter upper limit : "))
y = a
b = 1
x = 1
while y>=1 :
    b = b * y
    x = x + 1
    y = y - 1
    print("Factorial = %s " %(b))
    if (y==1):
        break

print("Final factorial = %s"%(b))

