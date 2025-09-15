a = int(input("Enter number : "))
b = 0
for i in range (0,a+1):
    b = b * 10
    b = b + (a % 10)
    if (a%100==b%10):
        break
    a = a//10
    

print(b)
