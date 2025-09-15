from tkinter import *

m = Tk()

r = Label(m, text = "This is a city")
r.pack()
photo = PhotoImage(file='butterfly.jpg')
w = Label(parent, image=photo)
w.photo = photo
w.pack()
mainloop()
