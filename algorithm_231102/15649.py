
import sys
n, m = [int(i) for i in sys.stdin.readline().split()]
nums = [i for i in range(1, n + 1)]


def dfs(path):
    if len(path) == m:
        print(*path)
        return
    for i in range(n):
        if nums[i] not in path:
            dfs(path + [nums[i]])


dfs([])
