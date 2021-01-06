sorted_list = [i for i in range(0, 10)]
print(sorted_list)


def binary_search_recursive(start, end, x):
    if start >= end:
        print("{} doesn't belong to list".format(x))
        return

    mid = int((start + end) / 2)
    if x == sorted_list[mid]:
        print("Found {} on position {}".format(x, mid))
        return
    elif x < sorted_list[mid]:
        end = mid
    else:
        start = mid + 1
    binary_search_recursive(start, end, x)


def binary_search(x):
    start = 0
    end = len(sorted_list)
    mid = int((start + end) / 2)

    while start < end:
        # print("start = {}, mid = {}, end = {}".format(start, mid, end))
        if x == sorted_list[mid]:
            print("Found {} on position {}".format(x, mid))
            break
        elif x < sorted_list[mid]:
            end = mid
        else:
            start = mid + 1
        mid = int((start + end) / 2)

    if start >= end:
        print("{} doesn't belong to list".format(x))


binary_search(11)
binary_search_recursive(0, len(sorted_list), 11)
