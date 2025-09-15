import random
q = 0
g = 0
a = []
for i in range (0,15):
    r = random.randint(1,100)
    q = q + r
    g = g+1
    a.append(r)

    
a.sort(reverse=False)
print(a)
print ("Median =" + str(a[7]))

v = q/g
print("Mean =" + str(v))










