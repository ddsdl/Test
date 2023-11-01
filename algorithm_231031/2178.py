# from collections import deque

# n, m = map(int, input().split(' '))
# g = []


# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))

#     direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

#     while queue:
#         x, y = queue.popleft()

#         for i in range(0, 4):
#             d_x, d_y = x + direction[i][0], y + direction[i][1]

#             if d_x <= -1 or d_y <= -1 or d_x >= n or d_y >= m:
#                 continue

#             if g[d_x][d_y] == 1:
#                 g[d_x][d_y] = g[x][y] + 1
#                 queue.append((d_x, d_y))


# for i in range(0, n):
#     g.append(list(map(int, input())))

# bfs(0, 0)

# print(g[n-1][m-1])

import sys
from collections import deque

n, m = [int(i) for i in sys.stdin.readline().split()]
maze = [[int(i) for i in sys.stdin.readline().rstrip()] for _ in range(n)]

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
queue = deque([[0, 0]])
while queue:
    x, y = queue.popleft()
    for i in direction:
        dx, dy = x+i[0], y+i[1]
        if 0 <= dx < n and 0 <= dy < m:
            if maze[dx][dy] == 1:
                maze[dx][dy] = maze[x][y] + 1
                queue.append([dx, dy])

# print("출발점 : ", maze[0][0])
print(maze[n-1][m-1])
