def selection_sorted(list):
    length = len(list)
    for x in range(length - 1):
        min = x
        for y in range(x + 1, length):
            if list[min] > list[y]:
                min = y
        list[x], list[min] = list[min], list[x]
    return list


print(selection_sorted([5, 4, 2, 6, 3, 1]))
