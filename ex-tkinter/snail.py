from tkinter import *

window = Tk()

canvas = Canvas(width=400, height=400)
canvas.pack()

x1 = 200
y1 = 200

text = canvas.create_text(x1, y1*2-20, text="Keys to move = a,d,w,s")


def draw_rect():
    canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill="green")


def del_rect():
    canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill="white")


def move(event):
    global x1, y1
    print(event.char)
    del_rect()
    if event.char == "a":
        x1 -= 10
    elif event.char == "d":
        x1 += 10
    elif event.char == "w":
        y1 -= 10
    elif event.char == "s":
        y1 += 10
    draw_rect()


window.bind("<Key>", move)


window.mainloop()

