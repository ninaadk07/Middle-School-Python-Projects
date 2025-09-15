a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

if a>b :
    for i in range (a,(a*b)+1):
        if i%a==0 and i%b==0 :
            print("LCM = " + str(i))
            break
else :
    for i in range (b,(a*b)+1):
        if i%a==0 and i%b==0 :
            print("LCM = " + str(i))
            break
    
