from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

window = Tk()
window.minsize(150, 100)
window.resizable(True, True)

my_list = [1, 65, 2, 9, 53, 24, 23, 55, 67]


def belongs_to_list(x):
    for i in range(0, len(my_list)):
        if my_list[i] == x:
            return True
    return False


answer = simpledialog.askinteger("Belongs to list", "Enter number:", minvalue=0, maxvalue=100)
element_belongs = belongs_to_list(answer)

if element_belongs:
    messagebox.showinfo("Correct!", "Element belongs to list!")
else:
    messagebox.showerror("Wrong!", "Element does NOT belong to list!")

window.mainloop()