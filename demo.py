list1 = [i for i in range(10, 20)]
x = int(input("x: "))
k = int(input("k: "))

list2 = []

print(list1)

# Metoda 1: cream o lista noua
# k = 3
# list1: 10 11 12 13 14 15 16 17 18 19
# list2: 10 11 12 99 13 14 15 16 17 18 19
# index: 0  1  2  3  4  5  6  7  8  9

for i in range(0, len(list1)):
    # Cand ajungem la pozitia potrivita => adaugam x
    if i == k:
        list2.append(x)
    # Adaugam toate elementele din list1 si in list3
    list2.append(list1[i])

print(list2)

# Metoda 2: inseram in aceeasi lista, deplasand elementele
# din dreapta pozitiei unde adagam in dreapta pentru
# a face loc elementului nou
# k = 3
# list1: 10 11 12 13 14 15 16 17 18 19 None
# list1: 10 11 12 13 13 14 15 16 17 18 19
# list1: 10 11 12 X  13 14 15 16 17 18 19

# crestem dimensiunea listei adaugand o celula goala la final
list1.append(None)

# Parcurgem de la dreapta la stanga si copiem elementele de dupa k la dreapta
for i in range(len(list1) - 1, k, -1):
    list1[i] = list1[i - 1]

# Adaugam noul element la pozitia potrivita.
list1[k] = x

print(list1)

