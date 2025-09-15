from tkinter import *

class App:

    def __init__(self,master):

        frame = Frame(master)
        frame.pack()

        self.button = Button (frame,text = "Quit", bg = "pink", command=frame.quit)
        self.button.pack(side=LEFT)

        self.buttontwo=Button(frame,text="Click here to win a car!", fg = "red", command=self.whatisthis)
        self.buttontwo.pack(side=RIGHT)

        self.woah=Button(frame,text = "5 foods that make you SOOO MUCH fatter!", bg = "black", fg = "gold", command = self.lol)
        self.woah.pack(side=RIGHT)

        self.question=Button(frame,text = "A lie ALL doctors keep telling you!", bg = "red" , fg = "blue", command = self.melol)
        self.question.pack(side=BOTTOM)

    def whatisthis(self):
        print("To win the car pay 2200000000000 dhs!!")

    def lol(self):
        print("Anything at McDonalds or KFC  ( : - ) )")

    def melol(self):
        print("An apple a day DOES NOT keep the doctors away")
    

        
        

root = Tk()

app = App(root)

root.mainloop()
root.destroy()
