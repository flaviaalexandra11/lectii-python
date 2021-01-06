

def is_even(elem):
    return elem % 2 == 0


def add2(elem):
    return elem + 2


def map(transform_func, list):
    for i in range(0, len(list)):
        list[i] = transform_func(list[i])


def filter(is_valid_func, list):
    for elem in list:
        if is_valid_func(elem) == False:
            list.remove(elem)


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    map(add2, my_list)
    print(my_list)

    filter(is_even, my_list)
    print(my_list)
