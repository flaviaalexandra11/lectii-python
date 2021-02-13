########################## Exemplu file.name ##########################

# Deschidem fisierul pentru citire ("r" - read)
input_file = open("input1.txt", "r")

# Citire intreg continut din fisier
str = input_file.read()

# Afisare nume fisier
print("Reading from file: {}".format(input_file.name))
print(str)

# Inchidere fisier
input_file.close()

# Deschidem fisierul pentru scriere ("w" - write)
output_file = open("output.txt", "w")

print("Writing in file: {}".format(output_file.name))
output_file.write(str)

# Inchidere fisier
output_file.close()
