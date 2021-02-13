from tkinter import *
from playsound import playsound

window = Tk()

do_btn = Button(text="DO", bg="white", fg="black", height=10, width=5, command=lambda: playsound("piano_notes/do.wav"))
do_btn.place(x=180, y=0)

re_btn = Button(text="RE", bg="white", fg="black", height=10, width=5, command=lambda: playsound("piano_notes/re.wav"))
re_btn.place(x=225, y=0)

mi_btn = Button(text="MI", bg="white", fg="black", height=10, width=5, command=lambda: playsound("piano_notes/mi.wav"))
mi_btn.place(x=270, y=0)

fa_btn = Button(text="FA", bg="white", fg="black", height=10, width=5, command=lambda: playsound("piano_notes/fa.wav"))
fa_btn.place(x=315, y=0)

sol_btn = Button(text="SOL", bg="white", fg="black", height=10, width=5, command=lambda: playsound("piano_notes/sol.wav"))
sol_btn.place(x=360, y=0)

la_btn = Button(text="LA", bg="white", fg="black", height=10, width=5, command=lambda: playsound("piano_notes/la.wav"))
la_btn.place(x=405, y=0)

si_btn = Button(text="SI", bg="white", fg="black", height=10, width=5, command=lambda: playsound("piano_notes/si.wav"))
si_btn.place(x=450, y=0)

do_btn = Button(text="DO", bg="white", fg="black", height=10, width=5, command=lambda: playsound("piano_notes/do-octave.wav"))
do_btn.place(x=495, y=0)


window.mainloop()