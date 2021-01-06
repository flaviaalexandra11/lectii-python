from tkinter import *


W_HEIGHT = 500
W_WIDTH = 500
window = Tk()
window.maxsize(width=W_WIDTH, height=W_HEIGHT)
window.minsize(width=W_WIDTH, height=W_HEIGHT)

C_HEIGHT = 400
C_WIDTH = 400

M_HEIGHT = 40
M_WIDTH = 40


canvas = Canvas(window, width=C_HEIGHT, height=C_WIDTH, bg="blue")
canvas.pack()

matrix = []

def draw_rect(x, y):
    print("({}, {})".format(x, y))
    canvas.create_rectangle(x, y, x + 10, y + 10, fill="black", width=0)

def init_map():
    global matrix
    line = [1] * M_WIDTH
    matrix.append(line)
    for y in range(1, M_HEIGHT - 1):
        line = [0] * M_WIDTH
        matrix.append(line)
    line = [1] * M_WIDTH
    matrix.append(line)


def print_matrix():
    global matrix
    for y in range(0, M_HEIGHT):
        for x in range(0, M_WIDTH):
            if matrix[y][x] == 1:
                draw_rect(x * 10, y * 10)


init_map()
print_matrix()

window.mainloop()