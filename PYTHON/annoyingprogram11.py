a = int(input("Enter lower limit : "))
b = int(input("Enter higher limit : "))
q = []
c = 0
for i in range (a,b+1):
    f = i**2
    q.append(f)
    c = c + f
    print (f)
    if (c>=300):
        break

    
