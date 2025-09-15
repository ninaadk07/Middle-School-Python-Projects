x = input("Enter the word : ")

a = []
b = [0,0,0,0,0]
y = len(x)
t = ""
h = len(x)
c = [0,0,0,0,0,0]
for i in range (0,h):

    a.append(x[i])

for j in range (0, y):
    v = input("Enter letter choice : ")
    
    for k in range (0,h):
        if v == a[k]: 
            print (v + " is a letter in this word ")
            if (v==b[k]):
                b = v[k]
                break
            b[k] = v
            y=y+1
            break
        elif (k==h) & (v!=a[k]):
            print (v + " is not a letter in this word ")

'''for g in range (0, h): 
    b[g] = c[g]'''            


if (j!=(y-1)):
    print("You got the word! It was : ")
    for p in range (0,h):
        t = str(t) + str(b[p])
else:
    
    print("Sorry, your turns are over")
    
print (t)
