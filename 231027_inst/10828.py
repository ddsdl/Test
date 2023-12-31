# n : 명령의 수
# n개만큼 명령이 주어진다
import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    command, *number = sys.stdin.readline().split()
    if command == 'push':
        stack.append(number[0])
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        pass