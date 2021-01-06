"""
    Ex3: Laturi triunghi
    Sa se citeasca 3 numere si sa se verifice daca acestea pot fi laturile unui triunghi 
    (suma a oricare 2 laturi trebuie sa fie mai mare ca a treia)
"""

x = int(input("Introduceti x: "))
y = int(input("Introduceti y: "))
z = int(input("Introduceti z: "))

# metoda 1
if x + y > z and x + z > y and y + z > x:
    print("Sunt laturile unui triunghi")
else:
    print("NU sunt laturile unui triunghi")

# metoda 2
if x + y < z or x + z < y or y + z < x:
    print("NU sunt laturile unui triunghi")
else:
    print("Sunt laturile unui triunghi")
