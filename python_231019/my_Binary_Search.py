def find_number(list, value):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2  # 반절 설정
        print(f"{value}의 값을 찾습니다.{start}와 {end} 사이에서")
        if value == list[mid]:
            return mid  # 인덱스 반환
        elif value > list[mid]:
            start = mid + 1  # 반절 오른쪽으로 재설정
        else:
            end = mid - 1   # 반절 왼쪽으로 재설정
    return -1


result = find_number([5, 1, 2, 54, 6, 4, 3, 4, 32,
                     21, 23, 4, 2, 6, 1, 22, 33], 7)
print(result)
