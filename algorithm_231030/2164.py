from collections import deque
import sys

# n = int(sys.stdin.readline().strip())
# queue = list(range(1, n + 1))

# while len(queue) > 1:
#     queue.pop(0)
#     front = queue.pop(0)
#     queue.append(front)

# print(queue[0])

# import sys

# n = int(sys.stdin.readline().strip())
# queue = [i for i in range(1, n + 1)]

# while len(queue) > 1:
#     queue.pop(0)
#     queue.append(queue.pop(0))

# print(*queue)
# print(queue[0])
# print(queue.pop())


n = int(sys.stdin.readline().strip())
queue = deque(range(1, n + 1))

while len(queue) > 1:
    queue.popleft()
    queue.rotate(-1)
    # queue.append(queue.popleft())

print(queue[0])
