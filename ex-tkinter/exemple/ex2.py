#### Creare buton care schimba textul unui label ####

def change_label():
    label.config(text="ALTCEVA")

# importam modulul tkinter
from tkinter import *

# cream o fereastra
window = Tk()

# dam un titlu ferestrei
window.title("Test")

# setam dimensiunea minima a ferestrei
window.minsize(500, 200)

# facem fereastra redimensionabila
window.resizable(True, True)

# creare label cu text
label = Label(text="CEVA")
label.pack()

# creare buton
button = Button(text="Butonul meu", command=change_label)
button.pack()

window.mainloop()