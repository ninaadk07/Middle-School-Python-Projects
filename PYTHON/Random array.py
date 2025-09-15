import random
f = []
g = []
x = 0
y = 0
for i in range (0,10):
    r = random.randint(1,100)
    print (r)
    f.append(r)
    x = x + r
    s = random.randint(1,100)
    print (s)
    g.append(s)
    y = y + s

print (x)
print (y)
z = x+y
print (z)
