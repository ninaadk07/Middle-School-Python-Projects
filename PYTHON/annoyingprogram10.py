import turtle

a = int(input("Enter size of array : "))
q = []
for i in range (1,a+1):
    b = (input("Enter colour : "))
    q.append(b)
    turtle.pencolor(b)
    turtle.forward(100)
    turtle.left(360/a)

print(q)
