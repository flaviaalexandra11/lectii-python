"""
    Ex4: Clasificare triunghi
    Sa se citeasca 3 numere reprezentand laturile unui triunghi si sa se determine daca triunghiul este: 
    - echilateral - are toate laturile de lungime egala
    - isoscel - are 2 laturi de lungime egala, a 3-a are o lungime diferita
    - oarecare - toate laturile au lungime diferita
"""

x = int(input("Introduceti x: "))
y = int(input("Introduceti y: "))
z = int(input("Introduceti z: "))

if x == y and y == z:
    print("Echilateral")
elif x == y or x == z or y == z:
    print("Isoscel") 
else:
    print("Oarecare")