from tkinter import *
from tkinter import colorchooser

window = Tk()
window.title("Drawing using shapes")
window.resizable(False, False)

C_HEIGHT = 512
C_WIDTH = 512

(start_x, start_y) = (0, 0)
color = "#476042"

canvas_shape = None
shape = "RECTANGLE"


def change_color(new_color):
    global color
    color = new_color


def choose_color():
    color_code = colorchooser.askcolor(title="Choose color")
    print(color_code)
    hex_format = color_code[1]
    change_color(hex_format)


def rect_pres():
    global shape
    shape = "RECTANGLE"


def circle_pres():
    global shape
    shape = "CIRCLE"


def line_pres():
    global shape
    shape = "LINE"


def on_press(event):
    """ Deseneaza un dreptunghi nou atunci cand userul da click pe canvas """
    global start_x, start_y, shape, canvas_shape

    # salveaza pozitia de start a dreptunghiului (unde a apasat userul)
    start_x = event.x
    start_y = event.y

    # creaza un un dreptunghi de latura 0
    if shape == "RECTANGLE":
        canvas_shape = canvas.create_rectangle(start_x, start_y, start_x, start_y, fill=color)
    elif shape == "CIRCLE":
        canvas_shape = canvas.create_oval(start_x, start_y, start_x, start_y, fill=color)
    elif shape == "LINE":
        canvas_shape = canvas.create_line(start_x, start_y, start_x, start_y, fill=color)


def on_move_press(event):
    """ Face resize la dreptunghiul creat mai devreme """

    # schimba coordonatele dreptunghiului la:
    # - coord de inceput - memorate in functia on_press
    # - coord curente - unde este mouse-ul acum
    canvas.coords(canvas_shape, start_x, start_y, event.x, event.y)


canvas = Canvas(width=C_WIDTH, height=C_HEIGHT, bg="white")
canvas.grid(row=2, columnspan=7)
canvas.bind("<ButtonPress-1>", on_press)
canvas.bind("<B1-Motion>", on_move_press)

button_black = Button(bg="black", width=10, command=lambda: change_color("black"))
button_red = Button(bg="red", width=10, command=lambda: change_color("red"))
button_green = Button(bg="green", width=10, command=lambda: change_color("green"))
button_blue = Button(bg="blue", width=10, command=lambda: change_color("blue"))
button_yellow = Button(bg="yellow", width=10, command=lambda: change_color("yellow"))
button_cyan = Button(bg="cyan", width=10, command=lambda: change_color("cyan"))
button_more = Button(text="More", width=10, command=choose_color)

button_black.grid(row=0, column=0)
button_red.grid(row=0, column=1)
button_green.grid(row=0, column=2)
button_blue.grid(row=0, column=3)
button_yellow.grid(row=0, column=4)
button_cyan.grid(row=0, column=5)
button_more.grid(row=0, column=6)

button_rect = Button(text="▭", width=10, command=rect_pres)
button_circle = Button(text="○", width=10, command=circle_pres)
button_line = Button(text="/", width=10, command=line_pres)

button_rect.grid(row=1, column=0)
button_circle.grid(row=1, column=1)
button_line.grid(row=1, column=2)

message = Label(window, text="Press and Drag the mouse to draw")
message.grid(row=3, columnspan=7)

mainloop()


