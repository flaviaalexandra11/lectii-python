########################## Exemplu read ##########################

# Deschidem fisierul pentru citire ("r" - read)
input_file = open("input1.txt", "r")

# Citire intreg continut din fisier
str = input_file.read()

print(str)

# Inchidere fisier
input_file.close()
