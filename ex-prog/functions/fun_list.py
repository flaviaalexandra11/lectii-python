'''
    Ex:Fun-List.
    Să se creeze următoarele funcții:
        - o funcție cu numele min_list care primește o lista și calculeaza cel mai mic element din listă
        - o funcție cu numele max_list care primește o lista și calculeaza cel mai mare element din listă
        - o funcție cu numele sum_list care primește o lista și calculeaza suma elementelor din listă
        - o funcție cu numele prod_list care primește o lista și calculeaza produsul elementelor din listă
'''


def min_list(my_list):
    my_min = my_list[0]
    for i in range(0, len(my_list)):
        if my_min > my_list[i]:
            my_min = my_list[i]
    return my_min


def sum_list(my_list):
    sum = 0
    for i in range(0, len(my_list)):
        sum = sum + my_list[i]
    return sum


some_list = [1, 2, -3, 4, 9, 23, 56, 5, 1, 9]

print(min_list(some_list))
print(sum_list(some_list))