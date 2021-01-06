"""
    Sum_n
    Să se citească de la un număr n și să se afișeze suma primelor n numere naturale. 
"""

# citim numarul de la tastatura si il transformam intr-un tip intreg
n = int(input("n = "))

# calculam suma -> formula: (primul + ultimul) * nr_termeni / 2
suma = (1 + n) * n / 2

print("Suma = {}".format(suma))