"""
    Number-Guesser
    Să se implementeze jocul Guess the number (Ghicește numărul):
        - va genera o variabila aleatoare care va trebui ghicita
        - numarul ghicit de noi se va citi intr-o bucla
        - dacă numărul citit este diferit de cel fixat se afișează Greșit și se trece la pasul urmator
        - dacă numărul citit este egal cu cel fixat se afișează  Corect și se oprește bucla
"""

import random

magic_number = random.randint(0, 100)
my_number = -1

while my_number != magic_number:
    my_number = int(input("Ghiceste: "))
    if my_number < magic_number:
        print("Prea mic...")
    else:
        print("Prea mare...")

print("Ai ghicit!")