from tkinter import *

window = Tk()

def copy():
    text_area.event_generate("<<Copy>>")

def cut():
    text_area.event_generate("<<Cut>>")

def paste():
    text_area.event_generate("<<Paste>>")

def clear():
    text_area.delete(1.0, END)


copy_button = Button(text="Copy", command=copy)
copy_button.pack()

cut_button = Button(text="Cut", command=cut)
cut_button.pack()

paste_button = Button(text="Paste", command=paste)
paste_button.pack()

clear_button = Button(text="Clear", command=clear)
clear_button.pack()

text_area = Text()
text_area.pack()

text_area.insert(1.0, "Hello from textbox!")

text = text_area.get(1.0, END)
print(text)

window.mainloop()