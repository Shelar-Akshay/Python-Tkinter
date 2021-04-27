from tkinter import *

w = Tk()

msg ='Hello from Tkinter'

i = Message(w, text = msg, bg='red')

i.pack()

w.mainloop()