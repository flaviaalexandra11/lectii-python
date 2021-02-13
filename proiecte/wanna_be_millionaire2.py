from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title("Wanna become a millionaire?")
window.minsize(150, 100)
window.resizable(True, True)

# TODO: afiseaza mesaj la consola si un messagebox showinfo - daca raspunsul e corect
#       afiseaza mesaj la consola si un messagebox showerror - daca e gresit


def check_answer():
    global idx, question, score, entry, question_label
    if entry.get() == answers[idx]:
        score += 1
        print("Corect! Scor: {}".format(score))
        messagebox.showinfo("Raspuns", "Corect!")

        entry.delete(0, END)        # sterge ce era in entry
        idx = random.randint(0, 5)  # alege alta intrebare
        question = questions[idx]
        question_label.config(text=question)
        hint_label.config(text="")
    else:
        print("Gresit! Scor: {}".format(score))
        messagebox.showerror("Raspuns", "Gresit!")
        hint_label.config(text=hints[idx])


questions = ["Cate planete are sistemul solar?",
             "Care este capitala Rusiei?",
             "Cine este presedintele Americii?",
             "In ce tara se afla Taj Mahal?",
             "Cum se numeau primele priamide?",
             "In ce tinut a fost imparat Tutankamon?"]

answers = ["9", "Moscova", "Trump", "India", "Zigurate", "Egipt"]

hints = ["Hint: ...intamplari ciudate si o minune (- 1)",
         "Hint: Incepe cu aceeasi litera ca 'Mama Rusie'",
         "Hint: Do you wanna build a waaaall?",
         "Hint: Bollywood",
         "Hint: Zzz",
         "Hint: faraon"]
score = 0

# Alege intrebarea
idx = random.randint(0, 5)
question = questions[idx]

# Afiseaza intrebarea
question_label = Label(window, text=question)
question_label.config(font="Arial 25")
question_label.pack()

hint_label = Label(window, text="")
hint_label.config(font="Arial 15")
hint_label.pack()

# Creeaza entry-ul pentru scrierea raspunsului
entry = Entry(window)
entry.config(font="Arial 15", bg="white", fg="green", bd=3, width=18)
entry.pack()

# Creeaza un buton cu textul "Verifica" care sa apeleze functia check_answer()
button = Button(window, command=check_answer, text="Verifica")
button.config(font="Arial 15", bg="red", fg="white")
button.pack()

window.mainloop()