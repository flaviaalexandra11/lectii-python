from tkinter import *
from playsound import playsound

window = Tk()
window.title("Jingle Bells")
window.minsize(710, 760)
window.resizable(False, False)

image = PhotoImage(file="piano_notes/jingle-bells.png")
label = Label(image=image)
label.place(x=0, y=0)

do_btn = Button(text="DO", bg="white", fg="black", height=10, width=5, command=lambda: playsound('piano_notes/do.wav'))
do_btn.place(x=180, y=600)

re_btn = Button(text="RE", bg="white", fg="black", height=10, width=5, command=lambda: playsound('piano_notes/re.wav'))
re_btn.place(x=225, y=600)

mi_btn = Button(text="MI", bg="white", fg="black", height=10, width=5, command=lambda: playsound('piano_notes/mi.wav'))
mi_btn.place(x=270, y=600)

fa_btn = Button(text="FA", bg="white", fg="black", height=10, width=5, command=lambda: playsound('piano_notes/fa.wav'))
fa_btn.place(x=315, y=600)

sol_btn = Button(text="SOL", bg="white", fg="black", height=10, width=5, command=lambda: playsound('piano_notes/sol.wav'))
sol_btn.place(x=360, y=600)

la_btn = Button(text="LA", bg="white", fg="black", height=10, width=5, command=lambda: playsound('piano_notes/la.wav'))
la_btn.place(x=405, y=600)

si_btn = Button(text="SI", bg="white", fg="black", height=10, width=5, command=lambda: playsound('piano_notes/si.wav'))
si_btn.place(x=450, y=600)

do1_btn = Button(text="DO", bg="white", fg="black", height=10, width=5, command=lambda: playsound('piano_notes/do-octave.wav'))
do1_btn.place(x=495, y=600)

do_btn_f = Button(text="DO#", bg="black", fg="white", height=4, width=3, command=lambda: playsound('piano_notes/do-f.wav'))
do_btn_f.place(x=205, y=600)

re_btn_f = Button(text="RE#", bg="black", fg="white", height=4, width=3, command=lambda: playsound('piano_notes/re-f.wav'))
re_btn_f.place(x=250, y=600)

fa_btn_f = Button(text="FA#", bg="black", fg="white", height=4, width=3, command=lambda: playsound('piano_notes/fa-f.wav'))
fa_btn_f.place(x=340, y=600)

sol_btn_f = Button(text="SOL#", bg="black", fg="white", height=4, width=3, command=lambda: playsound('piano_notes/sol-f.wav'))
sol_btn_f.place(x=385, y=600)

la_btn_f = Button(text="LA#", bg="black", fg="white", height=4, width=3, command=lambda: playsound('piano_notes/la-f.wav'))
la_btn_f.place(x=430, y=600)

window.mainloop()

