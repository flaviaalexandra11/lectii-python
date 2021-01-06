from tkinter import *

window = Tk()
window.title("hello")


def print_entry():
  print(entry.get())


entry = Entry(font="Arial 12", bg="white")
entry.pack()

button = Button(text="Print Entry", font="Arial 12", command=print_entry)
button.pack()

window.mainloop()