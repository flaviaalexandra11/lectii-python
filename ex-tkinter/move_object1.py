from tkinter import *
import random

WIDTH = 500
HEIGHT = 500

C_WIDTH = 400
C_HEIGHT = 400

OBSTACLES_COUNT = 20
obstacle_coords = []

window = Tk()
window.resizable(0, 0)
window.maxsize(WIDTH, HEIGHT)

canvas = Canvas(width=C_WIDTH, height=C_HEIGHT, bg="white")
canvas.pack()

x1 = 200
y1 = 200


instructionLabel = Label(text="Keys to move = a,d,w,s")
instructionLabel.pack()


def generate_obstacle_coords():
    for i in range(0, OBSTACLES_COUNT):
        x = random.randint(0, 5) * 10 + random.randint(0, 4) * 100
        y = random.randint(0, 5) * 10 + random.randint(0, 4) * 100
        obstacle_coords.append((x, y))


def draw_obstacles():
    for i in range(0, len(obstacle_coords)):
        (x, y) = obstacle_coords[i]
        canvas.create_rectangle(x, y, x + 10, y + 10, fill="black", width=0)


def draw_rect():
    canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill="green", width=0)


def del_rect():
    canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill="white", width=0)


def move(event):
    global x1, y1
    print(event.char)
    del_rect()
    if event.char == "a":
        if x1 >= 0:
            x1 -= 10
        else:
            x1 += C_WIDTH
    elif event.char == "d":
        if x1 <= C_WIDTH:
            x1 += 10
        else:
            x1 -= C_WIDTH
    elif event.char == "w":
        if y1 >= 0:
            y1 -= 10
        else:
            y1 += C_HEIGHT
    elif event.char == "s":
        if y1 <= C_HEIGHT:
            y1 += 10
        else:
            y1 -= C_HEIGHT
    draw_rect()
    if (x1, y1) in obstacle_coords:
        print("collision")

canvas.create_rectangle(20, 20, 20 + 10, 20 + 10, fill="black", width=0)
generate_obstacle_coords()
draw_obstacles()
canvas.focus_set()
canvas.bind("<Key>", move)
window.mainloop()

