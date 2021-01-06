'''
    Resources:
    - https://www.geeksforgeeks.org/make-notepad-using-tkinter/
    - https://www.tutorialspoint.com/python/tk_menu.htm
'''
# import os
# from tkinter import *

from tkinter.filedialog import *

def do_nothing():
    pass

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def cut():
    text_area.event_generate("<<Cut>>")

def open_file():
    global file
    file = askopenfilename(defaultextension=".txt")
    if file == "":
        file = None
    else:
        window.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, END)
        file = open(file, "r")
        text_area.insert(1.0, file.read())
        file.close()

def new_file():
    global file
    file = None
    window.title("Untitled - Notepad")
    text_area.delete(1.0, END)

def save_file():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt")
        if file == "":
            file = None
        else:
            file = open(file.name, "w")
            file.write(text_area.get(1.0, END))
            file.close()
            # Change the window title
            window.title(os.path.basename(file.name) + " - Notepad")
    else:
        file = open(file.name, "w")
        file.write(text_area.get(1.0, END))
        file.close()


window = Tk()
window.title("Untitled - Notepad")

menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About Notepad", command=do_nothing)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)

text_area = Text()
text_area.pack()

file = None

window.mainloop()