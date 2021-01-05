###################### Exemple input ######################

# Citire si afisare variabile a, b
a = input("a = ")
b = input("b = ")

print("Valoarea lui a este: {}".format(a))
print("Valoarea lui b este: {}".format(b))

print("Suma before: {}".format(a + b))

a = int(a)
b = int(b)
print("Suma after: {}".format(a + b))

# Reinitializare si convertire a, b
a = str(5)
b = int("5")


