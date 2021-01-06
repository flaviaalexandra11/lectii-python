from tkinter import *

window = Tk()
window.title("Bravest super hero")
window.resizable(True, True)

def introduce_hero():
    question_label.config(text=entry.get())

hero_image = PhotoImage(file="images/marvel-avatars/hero1.png")
question_label = Label(window, image=hero_image)
question_label.pack()

question_label = Label(window)
question_label.config(text="Enter text", font="Arial 20", fg="green")
question_label.pack(padx=50, pady=20)

entry = Entry(window)
entry.config(font="Arial 15", bg="white", fg="green", bd=3, width=18)
entry.pack()

button = Button(window, command=introduce_hero)
button.config(text="Present me", bg="black", fg="white", font="Arial 15", width=20, height=5)
button.pack()

window.mainloop()
