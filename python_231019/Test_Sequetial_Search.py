def find_number(list, value):
    where = []   # 찾을 값을 저장할 배열 생성

    for i in range(len(list)):  # 인덱스 0부터 배열 끝까지 반복문
        if value == list[i]:
            where.append(i)   # 찾는 값을 찾으면 where 배열에 저장

    return where    # 반복문 끝나면 where 배열을 반환


# user_input = input().split(" ")
# list = [int(i) for i in user_input]

list = list(map(int, input().split()))  # 사용자가 입력한 값을 1차원 배열로 저장
value = int(input())  # 찾을 값을 입력받음

result = find_number(list, value)
print(result)
