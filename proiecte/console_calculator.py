"""
    Console_calculator
    Se vor citi 2 numere a si b. 
    Se va afisa pe ecran cate un numar între 1 și 5 fiecare corespunzator unei operatii, astfel 
        (se afișează numărul și operația corespunzătoare): 
        0 - adunare         3 - impartire
        1 - scadere         4 - restul impartirii
        2 - inmultire
    Se va citi de la tastatură un număr op între 0 și 4.
    Se compara numărul citit cu fiecare dintre valorile posibile (0, 1, 2, 3, 4) folosind instrucțiunea if.
    Pentru fiecare caz se va calcula rezultatul corespunzător operației și se va afișa pe ecran.
"""
a = int(input("a = "))
b = int(input("b = "))
result = None

print("Operatii: ")
print("\t 0 - adunare")
print("\t 1 - scadere")
print("\t 2 - inmultire")
print("\t 3 - impartire")
print("\t 4 - modulo")

op = int(input("op = "))

if op == 0:
    result = a + b
elif op == 1:
    result = a - b
elif op == 2:
    result = a * b
elif op == 3:
    result = a / b
elif op == 4:
    result = a % b
else:
    print("Operatia nu exista!")

print("Rezultat: {}".format(result))