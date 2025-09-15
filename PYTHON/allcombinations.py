x=int(input("Enter 1st number : "))
y=int(input("Enter 2nd number : "))
z=int(input("Enter 3rd number : "))

a = [x,y,z]

for i in range (0,3):
    if a[i]>a[i-1]:
        p = a[i]
        a[i] = a[i-1]
        a[i-1] = p
        print (a)

    else :
        p = a[i-1]
        a[i-1] = a[i]
        a[i] = p
        print (a)

for q in range (1,3):
    
    if a[q]>a[q-1]:
        p = a[q]
        a[q] = a[q-1]
        a[q-1] = p
        print (a)


    elif a[q]<a[q-1]:
        p = a[q-1]
        a[q-1] = a[q]
        a[q] = p
        print (a)


for j in range (0,3):
    if a[j]>a[j-1] & a[j-1]<a[j-2]:
        p = a[j-1]
        a[j-1] = a[j]
        a[j] = p
        print (a)
        break
       
        
