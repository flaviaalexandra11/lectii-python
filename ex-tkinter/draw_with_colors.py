from tkinter import *
from tkinter import colorchooser

color = "gray"

def change_color(new_color):
    global color
    color = new_color


def paint(event):
    global color, v1
    x1 = (event.x - 1)
    y1 = (event.y - 1)
    x2 = (event.x + v1.get())
    y2 = (event.y + v1.get())
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def choose_color():
    global color
    color_code = colorchooser.askcolor(title="Choose color")
    hex_fromat = color_code[1]
    color = hex_fromat


window = Tk()
window.title("Painting using Ovals")

v1 = DoubleVar()

button_black = Button(bg="black", width=10, command=lambda: change_color("black"))
button_black.grid(row=0, column=0)

button_red = Button(bg="red", width=10, command=lambda: change_color("red"))
button_red.grid(row=0, column=1)

button_green = Button(bg="green", width=10, command=lambda: change_color("green"))
button_green.grid(row=0, column=2)

button_blue = Button(bg="blue", width=10, command=lambda: change_color("blue"))
button_blue.grid(row=0, column=3)

button_yellow = Button(bg="yellow", width=10, command=lambda: change_color("yellow"))
button_yellow.grid(row=0, column=4)

button_cyan = Button(bg="cyan", width=10, command=lambda: change_color("cyan"))
button_cyan.grid(row=0, column=5)

button_more = Button(text="More", width=10, command=choose_color)
button_more.grid(row=0, column=6)

canvas = Canvas(window, width=500, height=200, bg="white")
canvas.grid(row=1, columnspan=7)
canvas.bind("<B1-Motion>", paint)

scale = Scale(window, variable=v1, from_=1, to=100, orient=HORIZONTAL)
scale.grid(row=2, columnspan=7)

message = Label(window, text="Press and Drag the mouse to draw")
message.grid(row=3, columnspan=7)

mainloop()

