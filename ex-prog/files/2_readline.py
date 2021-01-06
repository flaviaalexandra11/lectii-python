########################## Exemplu readline ##########################

# Deschidem fisierul pentru citire ("r" - read)
input_file = open("input2.txt", "r")

# Citire nr de linii de text din fisier
# citim 1 linie pe care o transformam in int
nr_linii = int(input_file.readline())

print("Nr de linii de text: {}".format(nr_linii))

for i in range(0, nr_linii):
    str = input_file.readline()
    print("Linia {} este: {}".format(i+1, str), end="")

# Inchidere fisier
input_file.close()
