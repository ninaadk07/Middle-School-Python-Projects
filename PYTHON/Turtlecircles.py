import turtle
turtle.bgcolor("white")
turtle.colormode(255)
turtle.pencolor(110,31,124)
turtle.penup
turtle.setposition(0,-150)
turtle.pendown
for x in range (1,6):
    
    turtle.circle(x*25)
    turtle.penup()
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.pendown()
    
