# suma elem dintr-o lista
# produsul elem dintr-o lista
# media aritmetica a elem din lista
# maximul dintr-o lista
# minimul dintr-o lista


# suma primelor n numere
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)


result = sum(3)
print("Sum: {}".format(result))


# afisare inversa a unui cuvant
def inverse(word):
    if len(word) == 0:
        return
    print(word[len(word) - 1])
    inverse(word[:-1])


inverse("cuvant")

# factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# putere
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n-1)


result = power(2, 3)
print(result)