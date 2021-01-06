from tkinter import *
import random
window = Tk()
window.title("My Flag")
window.minsize(150, 100)
window.resizable(False, True)


def generate_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = "#%02x%02x%02x" % (red, green, blue)
    return color

rgb = generate_color()
question_label = Label(window)
question_label.config(height=100, width=50, bg=rgb)
question_label.pack(side=LEFT)

rgb = generate_color()
question_label = Label(window)
question_label.config(height=100, width=50, bg=rgb)
question_label.pack(side=RIGHT)

rgb = generate_color()
question_label = Label(window)
question_label.config(height=100, width=50, bg=rgb)
question_label.pack(side=TOP)

window.mainloop()