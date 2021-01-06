"""
    Ex5: Paritate
    Sa se citeasca un numar x si sa se determine daca acesta este par. 
    (Un numar este par, daca restul impartirii lui la 2 este egal cu 0)
    (Restul impartirii lui a la b in python: a % b).
    Daca este par, se va afisa x este par, altfel se va afisa x este impar.
"""

x = int(input("Introduceti x: "))

if x % 2 == 0:
    print("Par")
else:
    print("Impar")