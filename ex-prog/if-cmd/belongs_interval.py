"""
    Ex1: Sa se citeasca un numar x si 2 numere a si b.
    Daca x apartine intervalului [a, b] (x >= a si x <=b) sa se printeze x apartine [a, b],
        iar daca nu, sa se printeze x nu apartine [a, b].

    Ex2: Pornind de la Ex1, modificati astfel incaat atunci cand x nu apartine [a, b], 
    sa se afiseze daca x este mai mic decat a, sau mai mare decat b.

"""

x = int(input("Introduceti x: "))
a = int(input("Introduceti a: "))
b = int(input("Introduceti b: "))

if x >= a and x <= b:
    print("{} apartine [{}, {}]".format(x, a, b))
else:
    print("{} NU apartine [{}, {}]".format(x, a, b))
    if x < a:
        print("{} este mai mic decat {}".format(x, a))
    else:
        print("{} este mai mare decat {}".format(x, b))