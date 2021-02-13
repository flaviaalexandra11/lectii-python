from tkinter import *

def print_command(command):
    print(command)

window = Tk()
window.title("Menu bars")

menu_bar = Menu(window)

menu1 = Menu(menu_bar, tearoff=0)
menu2 = Menu(menu_bar, tearoff=0)
menu3 = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Menu 1", menu=menu1)
menu_bar.add_cascade(label="Menu 2", menu=menu2)
menu_bar.add_cascade(label="Menu 3", menu=menu3)

menu3.add_command(label="Command 1", command=lambda: print_command("command 1"))
menu3.add_command(label="Command 2", command=lambda: print_command("command 2"))
menu3.add_command(label="Command 3", command=lambda: print_command("command 3"))
menu3.add_separator()
menu3.add_command(label="Exit", command=window.quit)

window.config(menu=menu_bar)

window.mainloop()
