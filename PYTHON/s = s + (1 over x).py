x = (int(input("Enter the number : ")))
y = (int(input("Enter the limit : ")))
s = 0
for i in range (0, y+1):
    s = s + (1/(x+i))
    print (s)
print ("Final sume : %s " %s)
