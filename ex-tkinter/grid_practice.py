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
        index = col
        index = index + (row % 2) * (len(colors) - 1 - 2 * index)
        print("{} {} {}".format(row, col, index))
        color = colors[index]

        label = Label(text=str(counter), fg="white", bg=color)
        label.grid(row=row, column=col)
        counter = counter + 1
    print()

window.mainloop()