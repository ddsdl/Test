def find_my_number(list, value):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2  # 반절 설정
        if value == list[mid]:
            return mid  # 인덱스 반환
        elif value > list[mid]:
            start = mid + 1  # 반절 오른쪽으로 재설정
        else:  # 반절 왼쪽으로 재설정
            end = mid - 1
    return -1


result = find_my_number([i for i in range(1, 100+1)], 80)
print(result)
