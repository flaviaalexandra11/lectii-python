from tkinter import *


def print_command(command):
    print(command)


def change_color(color):
    canvas.itemconfig(square, fill=color)


def change_position(direction):
    global x1, y1, x2, y2
    print("Direction: {}".format(direction))
    if direction == "Left":
        canvas.move(square, -20, 0)
        x1 = x1 - 20
        x2 = x2 - 20
    elif direction == "Right":
        canvas.move(square, 20, 0)
        x1 = x1 + 20
        x2 = x2 + 20
    elif direction == "Up":
        canvas.move(square, 0, -20)
        y1 = y1 - 20
        y2 = y2 - 20
    elif direction == "Down":
        canvas.move(square, 0, 20)
        y1 = y1 + 20
        y2 = y2 + 20
    else:
        print("Error")


def change_size(command):
    global x1, y1, x2, y2

    if command == "Increase":
        x2 = x2 + 10
        y2 = y2 + 10
        canvas.coords(square, x1, y1, x2, y2)
    elif command == "Decrease":
        if x1 < x2 and y1 < y2:
            x2 = x2 - 10
            y2 = y2 - 10
        canvas.coords(square, x1, y1, x2, y2)
    else:
        print("Error")


wd = Tk()

menu_bar = Menu(wd)

color_menu = Menu(menu_bar, tearoff=0)
position_menu = Menu(menu_bar, tearoff=0)
size_menu = Menu(menu_bar, tearoff=0)
options_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Color", menu=color_menu)
menu_bar.add_cascade(label="Position", menu=position_menu)
menu_bar.add_cascade(label="Size", menu=size_menu)
menu_bar.add_cascade(label="Options", menu=options_menu)

color_menu.add_command(label="Yellow", command=lambda: change_color("Yellow"))
color_menu.add_command(label="Green", command=lambda: change_color("Green"))
color_menu.add_command(label="Blue", command=lambda: change_color("Blue"))
color_menu.add_command(label="Red", command=lambda: change_color("Red"))

position_menu.add_command(label="Left", command=lambda: change_position("Left"))
position_menu.add_command(label="Right", command=lambda: change_position("Right"))
position_menu.add_command(label="Up", command=lambda: change_position("Up"))
position_menu.add_command(label="Down", command=lambda: change_position("Down"))

size_menu.add_command(label="Increase", command=lambda: change_size("Increase"))
size_menu.add_command(label="Decrease", command=lambda: change_size("Decrease"))

options_menu.add_command(label="Exit", command=exit)

wd.config(menu=menu_bar)

canvas = Canvas()
canvas.pack()

x1 = 50
y1 = 50
x2 = 100
y2 = 100
square = canvas.create_rectangle(x1, y1, x2, y2, fill="red")

wd.mainloop()
