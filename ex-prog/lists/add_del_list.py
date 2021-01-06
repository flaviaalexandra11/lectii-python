
list = [i for i in range(0, 10)]


def insert_list(x, k):
    """ Insereaza un element x intr-o lista pe pozitia k """
    global list
    list.append(None)
    for i in range(len(list) - 1, k, -1):
        list[i] = list[i - 1]
    list[k] = x


def delete_from_list(k):
    """ Sterge elementul de pe pozitia k dintr-o lista  """
    global list
    for i in range(k, len(list) - 1):
        list[i] = list[i + 1]
    list = list[:-1]


print(list)

# Pentru stergere
# k = int(input("pozitia k = "))
# delete_from_list(k)

# Pentru inserare
x = int(input("elem nou x = "))
k = int(input("pozitia k = "))
insert_list(x, k)

print(list)
