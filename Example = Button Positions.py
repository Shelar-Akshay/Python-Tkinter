import tkinter
from tkinter import *
m = Tk()
redBtn = Button(m, text = "Red", fg = "red")
redBtn.pack( side = LEFT)
orangeBtn = Button(m, text = "Orange", fg = "black")
orangeBtn.pack( side = RIGHT )
blueBtn = Button(m, text = "Blue", fg = "blue")
blueBtn.pack( side = TOP )
blackBtn = Button(m, text = "Black", fg = "black")
blackBtn.pack( side = BOTTOM)
m.mainloop()
