
# cream lista si o afisam inainte de rotire
list = [i for i in range(0, 10)]
print(list)


def rot_left(K):
    global list
    # rotim de K ori la stanga
    for k in range(0, K):
        # salvam primul element
        first = list[0]
        # le copiem pe restul mai la stanga
        for i in range(0, len(list) - 1):
            list[i] = list[i + 1]
        # punem primul elment pe ultima pozitie
        list[len(list) - 1] = first


def rot_right(K):
    global list
    # rotim de K ori la dreapta
    for k in range(0, K):
        # salvam ultimul element
        last = list[len(list) -1]
        # le copiem pe restul mai la stanga
        for i in range(len(list) - 1, 0, -1):
            list[i] = list[i - 1]
        # punem ultimul elment pe prima pozitie
        list[0] = last


# citim numarul de rotiri K
K = int(input("K = "))

# rot_left(K)
rot_right(K)

# afisam lista dupa rotire
print(list)
