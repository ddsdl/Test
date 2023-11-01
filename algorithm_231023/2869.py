# 달팽이
# URL : https://www.acmicpc.net/problem/2869
# 풀이 시작 : 2023-10-23
# 풀이 완료 : 2023-10-23
import sys

A, B, V = [int(x) for x in sys.stdin.readline().split()]

day = int((V-A) / (A-B))
remainder = int((V-A) % (A-B))

if remainder == 0:
    print(day + 1)
elif remainder > 0:
    print(day + 2)
