from tkinter import *

m = Tk()
g = Tk()

def a():
    print ("Any nos. between 1 and 100")

def b():
    print ("This is totally not catfishing")

def c():
    print ("Chemotherapy")

def d():
    print ("www.netflix.com")

def e():
    print("Just earn them!")

def f():
    print("like seriously")

bone = Button(m, text="click to know the lottery numbers!",bg = "red", command=a)
bone.pack(side = LEFT)

btwo = Button(m, text = "Want to find beautiful girls?",bg ="light blue", command = b)
btwo.pack(side = RIGHT)

bthree = Button(m, text = "The way to cure cancer!",bg = "yellow", command = c)
bthree.pack(side = RIGHT)

bfour = Button(m, text = "Watch all recently released movies here (LEGAL)",bg = "light green", command = d)
bfour.pack(side = LEFT)

bfive = Button(m, text = "How to get lots of Youtube subscribers",bg = "pink", command = e)
bfive.pack(side = RIGHT)

bsix = Button(m, text = "im running out of ideas",bg = "orange", command = f)
bsix.pack(side = RIGHT)



mainloop()
