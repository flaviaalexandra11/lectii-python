from tkinter import *
from playsound import playsound

playsound('music_notes/DO.wav')

window = Tk()

do_btn = Button(text="DO")
do_btn.pack(side=LEFT)

do_btn_s = Button(text="DO#")
do_btn.pack(side=LEFT)
re_btn = Button(text="RE")
re_btn_s = Button(text="RE#")
mi_btn = Button(text="MI")
fa_btn = Button(text="FA")
fa_btn_s = Button(text="FA#")
sol_btn = Button(text="SOL")
sol_btn_s = Button(text="SOL#")
la_btn = Button(text="LA")
la_btn_s = Button(text="LA#")
si_btn = Button(text="SI")
do1_btn = Button(text="DO")

window.mainloop()