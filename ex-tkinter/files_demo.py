
# # Opening existing file for input
# input_file = open("files/input.txt", "r")
#
# # Reading input
# full_content = input_file.read()
# print("File content is: ")
# print(full_content)
#
# # Checking filename
# print("File name is: {}".format(input_file.name))
#
# # Closing file
# input_file.close()

#######################################################

# # Opening existing file for output
# output_file = open("files/output.txt", "w")
#
# # Writing in the output file
# output_file.write("This is an output file!")
#
# # Checking filename
# print("File name is: {}".format(output_file.name))
#
# # Closing file
# output_file.close()

#######################################################

# # Creating new file for output
# new_output_file = open("files/new_output.txt", "w")
#
# # Writing in the output file
# new_output_file.write("This is a new output file!")
#
# # Checking filename
# print("File name is: {}".format(new_output_file.name))
#
# # Closing file
# new_output_file.close()

#######################################################

# from tkinter import *
#
# window = Tk()
# window.title("Untitled - Notepad")
#
# menu_bar = Menu(window)
#
# menu1 = Menu(menu_bar, tearoff=0)
# menu2 = Menu(menu_bar, tearoff=0)
# menu3 = Menu(menu_bar, tearoff=0)
#
# menu_bar.add_cascade(label="Menu 1", menu=menu1)
# menu_bar.add_cascade(label="Menu 2", menu=menu2)
# menu_bar.add_cascade(label="Menu 3", menu=menu3)
#
# window.config(menu=menu_bar)
#
# window.mainloop()

#######################################################

from tkinter import *

def print_command(command):
    print(command)

window = Tk()
window.title("Untitled - Notepad")

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




