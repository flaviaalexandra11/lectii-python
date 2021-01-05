#### Creare fereastra cu text si imagine in Tkiter ####

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

# creare label cu imagine
image = PhotoImage(file="images/einstein.gif")
label1 = Label(image=image)
label1.pack()

# creare label cu text
explanation = "Use only GIF and PPM/PGM formats."
label2 = Label(text=explanation)
label2.pack()
