'''
    Resources:
    - https://www.geeksforgeeks.org/make-notepad-using-tkinter/
    - https://www.tutorialspoint.com/python/tk_menu.htm
    - https://www.geeksforgeeks.org/python-asksaveasfile-function-in-tkinter/
'''
# from tkinter import *

from tkinter.filedialog import *

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def cut():
    text_area.event_generate("<<Cut>>")

def open_file():
    global file
    file = askopenfilename()
    window.title(file + " - Notepad")
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
        files = [('All Files', '*.*'), ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes=files, defaultextension=files)
        print(file.name)

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
help_menu.add_command(label="About Notepad")
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)

text_area = Text()
text_area.pack()

file = None

window.mainloop()