"""
    Ex: Sa se citeasca dintr-un fisier numit patterns_input.txt un numar n.
    Intr-un fisier nou numit patterns_output.txt sa se afiseze un triunghi ca mai jos:

    pentru n = 3       Pentru n = 4
    *                  *
    **                 **
    ***                ***
    **                 ****
    *                  ***
                       **
                       *
"""

input_file = open("patterns_input.txt", "r")
n = int(input_file.read())
input_file.close()

output_file = open("patterns_output.txt", "w")

for i in range(1, n):
    for j in range(0, i):
        print("(i, j) = ({}, {})".format(i, j))
        output_file.write('*')
    output_file.write("\n")

print()

for i in range(n, 0, -1):
    for j in range(0, i):
        print("(i, j) = ({}, {})".format(i, j))
        output_file.write('*')
    output_file.write("\n")

output_file.close()
