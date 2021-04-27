from tkinter import *
w = Tk()
lb = Listbox(w)
lb.insert(1, 'Demo 1')
lb.insert(2, 'Demo 2')
lb.insert(3, 'Demo 3')
lb.insert(4, 'Demo 4')
lb.pack()
w.mainloop()