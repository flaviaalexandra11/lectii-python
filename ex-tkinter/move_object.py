import tkinter as tk

root = tk.Tk()

HEIGHT = 400
WIDTH = 400

canvas = tk.Canvas(root, width=HEIGHT, height=WIDTH)
canvas.pack()

x1 = 200
y1 = 200

text = canvas.create_text(x1, y1 * 2 - 20, text="Keys to move = a,d,w,s")

player = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10)


def move(event):
    global x1, y1
    print(canvas.coords(player))
    if event.char == "a":
        canvas.move(player, -10, 0)
    elif event.char == "d":
        canvas.move(player, 10, 0)
    elif event.char == "w":
        canvas.move(player, 0, -10)
    elif event.char == "s":
        canvas.move(player, 0, 10)


root.bind("<Key>", move)

root.mainloop()