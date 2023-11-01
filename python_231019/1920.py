# 수 찾기
# URL : https://www.acmicpc.net/problem/1920
# 풀이 시작 : 2023-10-19
# 풀이 완료 : 2023-10-19


def find_my_number(list, value):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2  # 반절 설정
        if value == list[mid]:
            return 1  # 있으면 1  반환
        elif value > list[mid]:
            start = mid + 1  # 반절 오른쪽으로 재설정
        else:  # 반절 왼쪽으로 재설정
            end = mid - 1
    return 0  # 없으면 0 반환


N = int(input())
N_list = sorted(list(map(int, input().split())))  # A[1],A[2] ... 정렬 배열
M = int(input())
M_list = list(map(int, input().split()))  # M개 배열 입력

for i in M_list:    # M배열 끝까지 반복 출력
    print(find_my_number(N_list, i))
