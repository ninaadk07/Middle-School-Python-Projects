a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

if (a<=b):
   n=a
else:
   n=b

while (n>=1):
    if (a%n==0) & (b%n==0):
        print("HCF = " + str(n))
        break
    else :
        n = n-1
        
    
