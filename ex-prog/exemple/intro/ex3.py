###################### Exemple operatori ######################

print("################# Numere intregi #################")

a = 5
b = 10
result = None

result = a + b
print("Suma: {}".format(result))
result = a - b
print("Diferenta: {}".format(result))
result = a * b
print("Produsul: {}".format(result))
result = a / b
print("Catul: {}".format(result))
result = a % b
print("Restul: {}".format(result))
result = a < b
print("Mai mic: {}".format(result))

print()

result = a <= b
print("Mai mic sau egal: {}".format(result))
result = a > b
print("Mai mare: {}".format(result))
result = a >= b
print("Mai mare sau egal: {}".format(result))
result = a == b
print("Egal: {}".format(result))
result = a != b
print("Diferit: {}".format(result))

print("################# Numere reale #################")

a = 5.0
b = 10.0
result = None

result = a + b
print("Suma: {}".format(result))
result = a - b
print("Diferenta: {}".format(result))
result = a * b
print("Produsul: {}".format(result))
result = a / b
print("Catul: {}".format(result))

print("################# Valori boolene #################")

a = True
b = False
result = None

result = not a
print("Not a: {}".format(result))
result = not b
print("Not b: {}".format(result))

result = a and b
print("And: {}".format(result))
result = a or b
print("Diferenta: {}".format(result))


print("################# Stringuri #################")

a = "Prima parte a stringului si... "
b = "a doua parte"
result = None

result = a + b
print("Concatenare: {}".format(result))
