# 수 찾기
# URL : https://www.acmicpc.net/problem/1920
# 풀이 시작 : 2023-10-19
# 풀이 완료 : 2023-10-19

def input_nums():
    _ = int(input())
    nums = [int(x) for x in input().split()]
    return nums


def find_linear_nums(a_nums, m_nums):
    for i in m_nums:
        result = 0
        for j in a_nums:
            if i == j:
                result = 1
                break
        print(result)


a_nums = input_nums()
m_nums = input_nums()
find_linear_nums(a_nums, m_nums)
