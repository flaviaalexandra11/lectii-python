"""
    Medie
    Citiți de la tastatură un număr 3 numere și afișați cu formatare, media lor aritmetică.
"""

# citim numerele si le transformam in tip de dare intreg
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

# calculam media
medie = (a + b + c) / 3

# afisam media
print("Media = {}".format(medie))