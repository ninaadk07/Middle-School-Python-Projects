import random

a = []
q=0
for i in range (0,5):
    r = random.randint(0,100)
    q = q+r
    a.append(r)
print (a)
f = 1
p = 0
g = 0
'''for m in range (0,5):
    
    
    if (a[m]>g):
        a[m] = p
        g = a[m]
        p = g

        a[m] = g
        
        if (i==4):
            break

print (a)'''

a.sort(reverse = True)

print (a)






        
'''b = []
for m in range (0,5):
    b.append(q/a[m])

h=0
for s in range (1,5):
    if b[s] > b[s-1]:
        b[s] = h
        b[s-1] = b[s]
        h = b[s-1]

print (b[0])'''

    

"""I gave up"""
