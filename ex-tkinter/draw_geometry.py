from tkinter import *
import random

C_WIDTH = 200
C_HEIGHT = 200
window = Tk()

colors = ['pink', 'cyan', 'magenta', 'blue', 'orange']
color_idx = 0

(x1, y1) = (None, None)
(x2, y2) = (None, None)


def draw_rect():
    global x1, x2, y1, y2
    global colors, color_idx
    color_idx = random.randint(0, len(colors) - 1)
    canvas.create_rectangle(x1, y1, x2, y2, fill=colors[color_idx])
    (x1, y1) = (None, None)
    (x2, y2) = (None, None)


def mouse_fun(event):
    global x1, y1, x2, y2
    print('Clicked at: ({} {})'.format(event.x, event.y))
    if x1 is None and x2 is None:
        x1 = event.x
        y1 = event.y
    elif x1 is not None and x2 is None:
        x2 = event.x
        y2 = event.y
        draw_rect()


canvas = Canvas(window, width=C_WIDTH, height=C_HEIGHT)
canvas.bind('<Button-1>', mouse_fun)
canvas.pack()

window.mainloop()