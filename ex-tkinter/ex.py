max = 10

def count(i):
    global max
    if i == max:
        return
    print(i)
    count(i+1)

count(0)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

res = factorial(3)

print(res)