from tkinter import *

window = Tk()

# Title & Window Size
window.title("Grid")
window.minsize(200, 75)
window.resizable(False, False)

label0 = Label(text="My grid")
label0.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

counter = 1
#           0       1       2        3
colors = ["red", "green", "blue", "violet"]

for row in range(1, 3):
    for col in range(0, 4):
        if row % 2 == 0:
            color = colors[col]
        else:
            color = colors[len(colors) - col - 1]

        label = Label(text=str(counter), fg="white", bg=color)
        label.grid(row=row, column=col)
        counter = counter + 1

window.mainloop()