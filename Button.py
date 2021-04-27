from tkinter import *
w = Tk()
btn=Button(w, text="This is Button widget",
fg='blue')
btn.place(x=10, y=20)
w.title('Hello Python')
w.geometry("300x200+10+10")
w.mainloop()