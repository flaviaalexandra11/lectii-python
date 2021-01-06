from tkinter import *
import random

W_WIDTH = 500
W_HEIGHT = 500
W_BG = '#F0F0F0'

C_WIDTH = 400
C_HEIGHT = 400
C_BG = 'white'

FOOD_COUNT = 20
food_x = []
food_y = []

SNAKE_SIZE = 3
SNAKE_COLOR = 'green'
snake_x = 200
snake_y = 200

window = Tk()
window.configure(bg=W_BG)
window.title('Snake')
window.resizable(0, 0)
window.maxsize(W_WIDTH, W_HEIGHT)
window.minsize(W_WIDTH, W_HEIGHT)

canvas = Canvas(width=C_WIDTH, height=C_HEIGHT, bg=C_BG)
canvas.pack()

instructionLabel = Label(text="Keys to move = w, a, s, d")
instructionLabel.pack()


def generate_obstacle_coords():
    pass


def draw_obstacles():
    pass


def draw_rect(x, y, color):
    canvas.create_rectangle(x, y, x + 10, y + 10, fill=color)


def del_rect(x, y):
    canvas.create_rectangle(x, y, x + 10, y + 10, fill=C_BG)


def is_collision(head_x, head_y):
    pass


def is_eating_tail():
    pass


def update_score():
    pass


def move(event):
    global snake_x, snake_y

    del_rect(snake_x, snake_y)

    if event.char == "a":
        snake_x -= 10
    elif event.char == "d":
        snake_x += 10
    elif event.char == "w":
        snake_y -= 10
    elif event.char == "s":
        snake_y += 10

    draw_rect(snake_x, snake_y, SNAKE_COLOR)



canvas.focus_set()
canvas.bind("<Key>", move)

generate_obstacle_coords()
draw_obstacles()

window.mainloop()

