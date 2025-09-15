from tkinter import *

m = Tk()

w = Canvas(m, width=400, height=400)
w.pack()


x = 100
y = 300
z = 300
q = 100

w.create_text(200,25, text = "HYPNOTISM TRICK *NEVER FAILS!!!*")

for i in range (0,20):
    if (i%2==0):
        t = "red"
    elif (i%2!=0):
        t = "gold"
    w.create_oval(x, y, z, q, fill=t)
    x = x + 5
    y = y - 5
    z = z - 5
    q = q + 5

mainloop()
