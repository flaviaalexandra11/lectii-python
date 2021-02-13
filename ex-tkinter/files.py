from tkinter import *
from tkinter.filedialog import *


def open_file():
    file = askopenfilename(defaultextension=".txt")
    if file == "":
        file = None
    else:
        file = open(file, "r")
        print(file.read())
        file.close()


def save_file():
    files = [('All Files', '*.*'), ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes=files, defaultextension=files)
    print(file.name)
    file = open(file.name, "w")
    file.write("Hello!")
    file.close()


window = Tk()
window.minsize(200, 200)

open_file_btn = Button(text="Open", command=open_file)
open_file_btn.pack()

save_file_btn = Button(text="Save", command=save_file)
save_file_btn.pack()


window.mainloop()