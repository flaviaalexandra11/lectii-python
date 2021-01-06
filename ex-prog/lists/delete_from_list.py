
# Crearea listei
list1 = [i for i in range(10, 20)]

# Citire k (pozitia unde inseram)
k = int(input("k: "))

print(list1)

# Metoda 1: cream o lista noua list2 in care adaugam toate
# elementele din list1 in afara de cel de pe pozitia k
# k = 3
# list1: 10 11 12 13 14 15 16 17 18 19
# list2: 10 11 12 14 15 16 17 18 19
# index: 0  1  2  3  4  5  6  7  8  9

# list2 = []

# for i in range(0, len(list1)):
#     if not i == k:
#         list2.append(list1[i])

# print(list2)

# Metoda 2: deplasam elementele din lista din dreapta elementului
# de pe pozitia k la stanga astfel incat sa suprascrie elementul de sters
# k = 3
# list1: 10 11 12 13 14 15 16 17 18 19
# list1: 10 11 12 14 15 16 17 18 19 _

# Parcurgem de la dreapta la stanga si copiem elementele de dupa k la dreapta
for i in range(0,len(list1) - 1):
    list1[i] = list1[i + 1]

# Scaderea numarului de elemente din lista (stergerea ultimului element)
list1 = list1[:-1]

print(list1)

