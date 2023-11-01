import heapq
import sys

n = int(sys.stdin.readline())

heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if not x:
        if heap:
            print(-(heapq.heappop(heap)))
        else:
            print(0)
    else:
        heapq.heappush(heap, -x)
