from tkinter import *
from tkinter import messagebox
import random

wd = Tk()


def verificare():
    global raspuns, intrebare, index
    if entry_raspuns.get() == raspuns:
        messagebox.showinfo("Raspuns", "Corect")
        entry_raspuns.delete(0, END)
        index = random.randint(0, len(intrebari) - 1)
        intrebare = intrebari[index]
        raspuns = raspunsuri[index]

        label_intrebare.config(text=intrebare)
    else:
        messagebox.showerror("Raspuns", "Gresit")

intrebari = ["Intrebare1", "Intrebare2", "Intrebare3"]
raspunsuri = ["Raspuns1", "Raspuns2", "Raspuns3"]

index = random.randint(0, len(intrebari) - 1)
intrebare = intrebari[index]
raspuns = raspunsuri[index]

wd.title("Vrei sa fi milionar")

label_titlu = Label(wd, text="Vrei sa fi milionar")
label_titlu.pack()

label_intrebare = Label(wd, text=intrebare)
label_intrebare.pack()

entry_raspuns = Entry(wd)
entry_raspuns.pack()

button_verificare = Button(wd, text="Verifica", command=verificare)
button_verificare.pack()

wd.mainloop()

