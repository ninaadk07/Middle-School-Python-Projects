x = int(input("Enter number : "))

def fibonacci(x):
    if (x<=1):
        return x
    else:
        d = 0
        b = ((fibonacci(x-1))) + ((fibonacci(x-2)))
        return b


for i in range (0,x):
    print ((fibonacci(i)))
    
