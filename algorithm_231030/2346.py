import sys
from collections import deque

# n = int(sys.stdin.readline())

# queue = deque(enumerate([int(i) for i in sys.stdin.readline().split()]))

# for i in range(n):
#     p = queue.popleft()
#     print(p[0], end=' ')
#     if p[1] > 0:
#         queue.rotate(-(p[1] - 1))
#     else:
#         queue.rotate(-p[1])

# from collections import deque

# n = int(input())
# num = list(map(int, input().split()))
# balloon = [(i+1, num[i]) for i in range(n)]
# result = []
# cnt = 0
# balloon_queue = deque(balloon)

# for _ in range(n-1):
#     result.append(balloon_queue[cnt][0])
#     c = balloon_queue[cnt][1]
#     balloon_queue.remove(balloon_queue[cnt])
#     if c >= 0:
#         cnt = (cnt + c - 1) % len(balloon_queue)
#     else:
#         cnt = (cnt + c) % len(balloon_queue)

# result.append(balloon_queue[cnt][0])
# for r in result:
#     print(r, end=' ')

# import sys
# from collections import deque

# n = int(sys.stdin.readline())
# balloon = deque([int(i) for i in sys.stdin.readline().split()])


n = int(sys.stdin.readline())

balloon = deque(enumerate([int(i)
                for i in sys.stdin.readline().split()], start=1))

result = []
while balloon:
    index, move = balloon.popleft()
    if move > 0:
        balloon.rotate(-(move - 1))
    else:
        balloon.rotate(-move)

print(' '.join(map(str, result)))
