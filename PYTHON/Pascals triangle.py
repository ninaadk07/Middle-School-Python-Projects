e = int(input("End limit: "))
a = []
print("[1]")
a.append(1)
a.append(1)
print(a)
c = [1]
x = 1
for j in range (0,e-2):
    if (j!=0):
        a.append(1)
        c.append(1)
    for i in range (1, x + 1):
        if (x%2!=0):
            v = ((a[i-1]) + (a[i]))
            c.append(v)
        elif (x%2==0):
           f = ((c[i-1])+(c[i]))
           a.append(f)
        if (i==x):
            if (x%2!=0):
                c.append(1)
                print(c)
                a.clear()
            elif (x%2==0):
                a.append(1)
                print(a)
                c.clear()
            
            x = x + 1
            break
    

'''e = int(input("End limit: "))
a = []
print("[1]")
a.append(1)
a.append(1)
print(a)
c = [1]
x = 1
for j in range (0,e-2):
    if (j!=0):
        a.append(1)
        c.append(1)
        def pascal(i,x,c,v,a,f):
            
            for i in range (1, x + 1):
                if (x%2!=0):
                    v = ((a[i-1]) + (a[i]))
                    c.append(v)
                    return c
                elif (x%2==0):
                   f = ((c[i-1])+(c[i]))
                   return a
                break
        
    if (i==x):
        if (x%2!=0):
            c.append(1)
            print(pascal(i,x,c,v,a,f))
            a.clear()
        elif (x%2==0):
            a.append(1)
            print(pascal(i,x,c,v,a,f))
            c.clear()
            
            x = x + 1
            break'''
    
