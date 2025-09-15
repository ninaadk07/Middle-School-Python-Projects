"""a = int(input("Enter size of array : "))
q = []
for i in range (0,a):
    b = input("enter a word : ")
    q.append(b)
    q.sort(key=len)
    
print(q)"""

"""a = int(input("Enter size of array : "))
q = []
for i in range (0,a):
    b = int(input("Enter a number : "))
    q.append(b)
    q.sort()

print(q[a-2])"""

"""q = []
for i in range (0,101):
    q.append(i)
    if (q[i]%5==0) or (q[i]%7==0):
        print (q[i])"""

import random

a = int(input("Enter size of array : "))
q = []
c = 0
for i in range (0,a):
    r = random.randint(1,100)
    q.append(r)
    print (q[i])
    c = c + r

print (c)
