#### Creare fereastra cu text si imagine in Tkiter ####

from tkinter import *

def change_text():
    label_text = "Happy new year!"
    label.config(text=label_text)

window = Tk()
window.title("Christmas Card")
window.minsize(500, 200)
window.resizable(True, True)
window.configure(background='cyan')

label_text = "Merry Christmas"
title_label = Label(text=label_text, font="Cambria 25", fg="#b30000")
title_label.pack()

image = PhotoImage(file="images/image1.png")
img_label = Label(image=image)
img_label.pack()

label_text = "Unwrap yourself a joyful Christmas!"
label = Label(text=label_text, font="Cambria 16", fg="#b30000")
label.pack()

button_text = ">"
button = Button(text=button_text, font="Cambria 16", fg="#b30000", command=change_text)
button.pack()
