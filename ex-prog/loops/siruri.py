'''
    Siruri.
    Sa se afiseze pe ecran folosind functia for si range urmatoarele siruri:
'''

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(0, 10):
    print('{} '.format(i), end='')
print()

# 0, 2, 4, 6, 8
for i in range(0, 10, 2):
    print('{} '.format(i), end='')
print()

# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
for i in range(10, 0, -1):
    print('{} '.format(i), end='')
print()

# 9, 7, 5, 3, 1
for i in range(9, 0, -2):
    print('{} '.format(i), end='')
print()