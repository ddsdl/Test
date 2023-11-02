import sys
n = int(sys.stdin.readline())

member = []

for _ in range(n):
    age, name = map(str, sys.stdin.readline().split())
    member.append((int(age), name))

member.sort(key=lambda x: x[0])

for age, name in member:
    print(age, name)
