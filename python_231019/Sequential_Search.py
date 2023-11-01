def find_my_number(list, value):
    count = 0
    length = len(list)
    for i in range(length):
        count += 1
        if value == list[i]:
            print(f"{count}번 만에 찾았습니다.")
            return i
    return -1


result = find_my_number([5, 2, 6, 1, 2, 3, 4, 7, 9, 1, 5], 9)
print(result)
