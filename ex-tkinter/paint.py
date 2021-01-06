from tkinter import *

window = Tk()

v1 = DoubleVar()


def show_scale():
    global v1
    print(v1.get())


s1 = Scale(window, variable=v1, from_=1, to=100, orient=HORIZONTAL)
s1.pack(anchor=CENTER)

b1 = Button(text="Show scale", command=show_scale)
b1.pack()

l1 = Label()
l1.pack()

window.mainloop()