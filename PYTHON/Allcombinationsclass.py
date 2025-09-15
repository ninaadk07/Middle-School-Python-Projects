
x=int(input("Enter 1st number : "))
y=int(input("Enter 2nd number : "))
z=int(input("Enter 3rd number : "))
d=int(input("Enter 4th number : "))

a = [y,z,d]

p = 0

v = [x]
for i in range (0,3):
    if a[i]>a[i-1]:
        p = a[i]
        a[i] = a[i-1]
        a[i-1] = p
        v.append(a)
        print (v)
        v = [x]

    else :
        p = a[i-1]
        a[i-1] = a[i]
        a[i] = p
        v.append(a)
        print (v)
        v = [x]

for q in range (1,3):
    
    if a[q]>a[q-1]:
        p = a[q]
        a[q] = a[q-1]
        a[q-1] = p
        v.append(a)
        print (v)
        v = [x]


    elif a[q]<a[q-1]:
        p = a[q-1]
        a[q-1] = a[q]
        a[q] = p
        v.append(a)
        print (v)
        v = [x]


for j in range (0,3):
    if a[j]>a[j-1] & a[j-1]<a[j-2]:
        p = a[j-1]
        a[j-1] = a[j]
        a[j] = p
        v.append(a)
        print (v)
        v = [x]
        break

a = [x,z,d]

v = [y]

for i in range (0,3):
    if a[i]>a[i-1]:
        p = a[i]
        a[i] = a[i-1]
        a[i-1] = p
        v.append(a)
        print (v)
        v = [y]

    else :
        p = a[i-1]
        a[i-1] = a[i]
        a[i] = p
        v.append(a)
        print (v)
        v = [y]

for q in range (1,3):
    
    if a[q]>a[q-1]:
        p = a[q]
        a[q] = a[q-1]
        a[q-1] = p
        v.append(a)
        print (v)
        v = [y]


    elif a[q]<a[q-1]:
        p = a[q-1]
        a[q-1] = a[q]
        a[q] = p
        v.append(a)
        print (v)
        v = [y]


for j in range (0,3):
    if a[j]>a[j-1] & a[j-1]<a[j-2]:
        p = a[j-1]
        a[j-1] = a[j]
        a[j] = p
        v.append(a)
        print (v)
        v = [y]
        break

a = [x,y,d]
v = [z]

for i in range (0,3):
    if a[i]>a[i-1]:
        p = a[i]
        a[i] = a[i-1]
        a[i-1] = p
        v.append(a)
        print (v)
        v = [z]

    else :
        p = a[i-1]
        a[i-1] = a[i]
        a[i] = p
        v.append(a)
        print (v)
        v = [z]

for q in range (1,3):
    
    if a[q]>a[q-1]:
        p = a[q]
        a[q] = a[q-1]
        a[q-1] = p
        v.append(a)
        print (v)
        v = [z]


    elif a[q]<a[q-1]:
        p = a[q-1]
        a[q-1] = a[q]
        a[q] = p
        v.append(a)
        print (v)
        v = [z]


for j in range (0,3):
    if a[j]>a[j-1] & a[j-1]<a[j-2]:
        p = a[j-1]
        a[j-1] = a[j]
        a[j] = p
        v.append(a)
        print (v)
        v = [z]
        break

a = [x,y,z]
v = [d]

for i in range (0,3):
    if a[i]>a[i-1]:
        p = a[i]
        a[i] = a[i-1]
        a[i-1] = p
        v.append(a)
        print (v)
        v = [d]

    else :
        p = a[i-1]
        a[i-1] = a[i]
        a[i] = p
        v.append(a)
        print (v)
        v = [d]

for q in range (1,3):
    
    if a[q]>a[q-1]:
        p = a[q]
        a[q] = a[q-1]
        a[q-1] = p
        v.append(a)
        print (v)
        v = [d]


    elif a[q]<a[q-1]:
        p = a[q-1]
        a[q-1] = a[q]
        a[q] = p
        v.append(a)
        print (v)
        v = [d]


for j in range (0,3):
    if a[j]>a[j-1] & a[j-1]<a[j-2]:
        p = a[j-1]
        a[j-1] = a[j]
        a[j] = p
        v.append(a)
        print (v)
        v = [d]
        break
    
'''
for i in range (0,4):
    
    if a[i]>a[i-1]:
        a = [x,y,z,d]
        a[i] = p
        a[i-1] = a[i]
        p = a[i-1]
        print(a)

    else :
        p = a[i-1]
        a[i-1] = a[i]
        a[i] = p
        print (a)

a = [x,y,z,d]

for j in range (0,5):
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
    if a[i]<a[i+1]:
        a = [x,y,z,d]
        a[i] = p
        a[i+1] = a[i]
        p = a[i+1]
        print(a)
        

1,2,3,4
   1,3,4,2
   1,2,4,3
   1,3,2,4
   1,4,2,3
   1,4,3,2
   2,1,3,4
   2,1,4,3
   2,3,1,4
   2,3,4,1
   2,4,1,3
   2,4,3,1
   3,1,2,4
   3,1,4,2
   3,2,1,4
   3,2,4,1
   3,4,1,2
   3,4,2,1
   4,1,2,3
   4,1,3,2
   4,2,1,3
   4,2,3,1
   4,3,1,2
   4,3,2,1'''

        
