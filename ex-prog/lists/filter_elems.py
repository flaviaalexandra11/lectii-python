'''
    Filter-Elems
    Se da o lista, sa se afiseze doar elementele pare si divizibile cu 3.
'''

my_list = [1, 22, 3, 19, 2, 18, 16, 5, 8, 16, 4, 13, 34, 11, 7]

for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0 and my_list[i] % 3 == 0:
        print(my_list[i])
