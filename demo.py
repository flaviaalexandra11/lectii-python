from tkinter import *
from tkinter.filedialog import *

def new_file():
    global file
    file = None
    text_area.delete(1.0, END)

def open_file():
    global file
    # deschidem dialog
    file = askopenfilename(defaultextension=".txt")
    # golim textarea
    text_area.delete(1.0, END)
    # deschidem si citim din fisier
    file = open(file, "r")
    text = file.read()
    # inseram in textarea ce am citit din fisier
    text_area.insert(1.0, text)
    # inchidem fisierul
    file.close()

def save_file():
    global file
    # daca nu avem un fisier deschis => cream deialog de salvare
    if file is None:
        files = [('All files', '*.*'), ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes=files, defaultextension=files)
        print(file.name)
    # deschidem fiserul
    file = open(file.name, "w")
    # luam datele din textarea
    text = text_area.get(1.0, END)
    # scriem datele in fiser
    file.write(text)
    # inchidem fiserul
    file.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

window = Tk()
window.title("Untitled - Notepad")

menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
edit_menu = Menu(menu_bar, tearoff=0)
help_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu.add_command(label="About Notepad")

text_area = Text()
text_area.pack()

file = None

window.config(menu=menu_bar)
window.mainloop()