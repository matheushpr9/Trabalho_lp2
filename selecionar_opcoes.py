from tkinter import *

master = Tk()

variable = StringVar(master)
 # default value

a = ["one", "two", "three"]
variable.set(a[0])
w = OptionMenu(master, variable, *a)
w.pack()

mainloop()