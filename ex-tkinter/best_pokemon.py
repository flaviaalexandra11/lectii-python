from tkinter import *

window = Tk()
window.title("Best Pokemon")
window.minsize(400, 400)
window.resizable(True, True)

pokemon_name = "Charizard"
question_label = Label(window, text=pokemon_name)
question_label.config(font="Arial 30", fg="red")
question_label.pack(side=TOP)

power_type = "Fire/Flying-type"
question_label = Label(window, text=power_type)
question_label.config(font="Arial 20", fg="white", bg="black")
question_label.pack()

evolved_from = "Evolved from: Charmeleon"
question_label = Label(window, text=evolved_from)
question_label.config(font="Arial 20", fg="white", bg="black")
question_label.pack()

pokemon_image = PhotoImage(file="images/pokemons/charizard.png")
question_label = Label(window, image=pokemon_image)
question_label.pack()

fun_fact = "It is said that Charizard's fire burns hotter if it has experienced harsh battles."
question_label = Label(window, text=fun_fact)
question_label.config(font="Arial 20", fg="white", bg="black")
question_label.pack()
window.mainloop()
