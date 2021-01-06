from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

window = Tk()

my_number = simpledialog.askinteger("Numar", "Introdu un numar")
print(my_number)


my_list = [0, 12, 24, 35, 43, 54, 64, 74, 84, 94]

found = False

start = 0
end = len(my_list)
mid = int((start + end) / 2)

while start < end:
    print("start = {}, mid = {}, end = {}".format(start, mid, end))
    if my_number == my_list[mid]:
        found = True
        break
    elif my_number < my_list[mid]:
        end = mid
    else:
        start = mid + 1
    mid = int((start + end) / 2)


if found:
    messagebox.showinfo("Info", "Numarul face parte din lista")
else:
    messagebox.showerror("Eroare", "Numarul nu face parte din lista")

window.mainloop()