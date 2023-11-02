# import sys
# n, m = int(sys.stdin.readline().split())
# num = []


# def dfs(n, m):
#     if len(num) == m:
#         print(" ".join([str(x)for x in num]))
#         return
#     for i in range(1, n+1):
#         num.append(i)
#         dfs(n, m)


# n, m = map(int, input().split())
# num = [i+1 for i in range(n)]  # 1 2 3
# result = [0 for _ in range(m)]


# def dfs(idx):
#     if idx >= m:  # 1 >= 1
#         print(*result)
#         return
#     for i in range(n):
#         result[idx] = num[i]  # [1,2,3 ]
#         dfs(idx + 1)


# dfs(0)

import sys
n, m = [int(i) for i in sys.stdin.readline().split()]
nums = [i for i in range(1, n + 1)]


def dfs(nums, path):
    if len(path) == m:
        print(*path)
        return
    for i in range(n):
        dfs(nums, path + [nums[i]])


dfs(nums, [])
