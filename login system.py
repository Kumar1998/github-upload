from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to Class")
window.geometry('500x500')
window.configure(background ="grey");
a = Label(window,text = "First Name").grid(row = 0,column = 0)
b = Label(window,text = "Last Name").grid(row = 1,column = 0)
c = Label(window,text = "Email id").grid(row = 2,column = 0)
d = Label(window,text = "Contact Number").grid(row = 3,column = 0)
a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 2)
c1 = Entry(window).grid(row = 2,column = 2)
d1 = Entry(window).grid(row=3,column = 1)
def clicked():
    res = "Welcome to"+txt-get()
    lbl.configure(text=res)
btn = ttk.Button(window,text = "submit").grid(row = 4,column = 0)
window.mainloop()    