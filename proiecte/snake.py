from tkinter import *
import random

W_WIDTH = 500
W_HEIGHT = 500
W_BG = 'black'

C_WIDTH = 400
C_HEIGHT = 400
C_BG = '#000080'

FOOD_COUNT = 20
SCORE = 0
SCORE_STRING = "Score: " + str(SCORE)
food_x = []
food_y = []

SNAKE_SIZE = 3
snake_x = [200, 210, 220]
snake_y = [200, 200, 200]

window = Tk()
window.configure(bg=W_BG)
window.title('Snake')
window.resizable(0, 0)
window.maxsize(W_WIDTH, W_HEIGHT)
window.minsize(W_WIDTH, W_HEIGHT)

scoreLabel = Label(text=SCORE_STRING, font="Terminal 25", fg='red', bg='black', pady=10)
scoreLabel.pack()

canvas = Canvas(width=C_WIDTH, height=C_HEIGHT, bg=C_BG)
canvas.pack()

instructionLabel = Label(text="Keys to move = w, a, s, d", font="Terminal 15", fg='red', bg='black', pady=10)
instructionLabel.pack()


def generate_obstacle_coords():
    for i in range(0, FOOD_COUNT):
        x = random.randint(0, 5) * 10 + random.randint(0, 4) * 100
        y = random.randint(0, 5) * 10 + random.randint(0, 4) * 100
        food_x.append(x)
        food_y.append(y)


def draw_obstacles():
    for i in range(0, FOOD_COUNT):
        x = food_x[i]
        y = food_y[i]
        canvas.create_rectangle(x, y, x + 10, y + 10, fill="red", width=0)


def draw_rect(x, y, color):
    canvas.create_rectangle(x, y, x + 10, y + 10, fill=color, width=0)


def del_rect(x, y):
    canvas.create_rectangle(x, y, x + 10, y + 10, fill=C_BG, width=0)


def is_collision(head_x, head_y):
    for i in range(0, FOOD_COUNT):
        if head_x == food_x[i] and head_y == food_y[i]:
            print("Collision")
            return True
    return False


def is_eating_tail():
    head_x = snake_x[0]
    head_y = snake_y[0]
    for i in range(1, SNAKE_SIZE):
        if head_x == snake_x[i] and head_y == snake_y[i]:
            print("Eating tail")
            return True
    return False


def update_score():
    global SCORE, SCORE_STRING
    SCORE += 1
    SCORE_STRING = "Score: " + str(SCORE)
    scoreLabel.config(text=SCORE_STRING)


def move(event):
    global SNAKE_SIZE, snake_x, snake_y, last_move

    # ultimul patrat din coada
    # (vom folosi daca creste sarpele sau cand ne deplasam - del_rect)
    tail_x = snake_x[SNAKE_SIZE -1]
    tail_y = snake_y[SNAKE_SIZE -1]

    # deplasare coada
    if SNAKE_SIZE > 1:
        for i in range(SNAKE_SIZE - 1, 0, -1):
            snake_x[i] = snake_x[i - 1]
            snake_y[i] = snake_y[i - 1]
            draw_rect(snake_x[i], snake_y[i], "#00ff00")

    # deplasare cap
    if event.char == "a":
        if snake_x[0] >= 0:
            snake_x[0] -= 10
        else:
            snake_x[0] += C_WIDTH
    elif event.char == "d":
        if snake_x[0] <= C_WIDTH:
            snake_x[0] += 10
        else:
            snake_x[0] -= C_WIDTH
    elif event.char == "w":
        if snake_y[0] >= 0:
            snake_y[0] -= 10
        else:
            snake_y[0] += C_HEIGHT
    elif event.char == "s":
        if snake_y[0] <= C_HEIGHT:
            snake_y[0] += 10
        else:
            snake_y[0] -= C_HEIGHT
    draw_rect(snake_x[0], snake_y[0], '#00cc00')
    del_rect(tail_x, tail_y)

    # crestere daca mananca
    if is_collision(snake_x[0], snake_y[0]):
        snake_x.append(tail_x)
        snake_y.append(tail_y)
        SNAKE_SIZE += 1
        draw_rect(tail_x, tail_y, '#00ff00')
        update_score()

    if is_eating_tail():
        window.destroy()


canvas.focus_set()
canvas.bind("<Key>", move)

generate_obstacle_coords()
draw_obstacles()

window.mainloop()

