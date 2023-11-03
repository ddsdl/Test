# import sys

# n, m = map(int, sys.stdin.readline().split())
# money = [int(i) for i in sys.stdin.readline().split()]

# max_money = sum(money[:m])

# for i in range(n):
#     max_money = max(max_money, max_money - money[i - m] + money[i])
# print(max_money)

import sys

n, m = [int(i) for i in sys.stdin.readline().split()]
money = [int(i) for i in sys.stdin.readline().split()]


max_money = sum(money[:m])

sum = max_money
for i in range(m, n):
    sum = sum - money[i - m] + money[i]
    max_money = max(max_money, sum)

print(max_money)
