# import sys
# input = sys.stdin.readline

# case = int(input())

# for _ in range(case):
#     n = int(input())
#     dict = {}

#     for _ in range(n):
#         name, kind = input().split()
#         if kind in dict:
#             dict[kind] += 1
#         else:
#             dict[kind] = 1

#     result = 1

#     for i in dict.values():
#         result *= (i + 1)

#     print(result - 1)

from collections import Counter
import sys

n = int(sys.stdun.readline())

case = int(sys.stdin.readline())

for i in range(case):
    n = int(sys.stdin.readline())
