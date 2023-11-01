# import sys
# class Stack:
#     def __init__(self):
#         self.len = 0
#         self.list = []

#     def push(self, num):
#         self.list.append(num)
#         self.len += 1

#     def pop(self):
#         if self.size() == 0:
#             return -1
#         result = self.list[self.len - 1]
#         del self.list[self.len - 1]
#         self.len -= 1
#         return result

#     def size(self):
#         return self.len

#     def empty(self):
#         if self.len == 0:
#             return 1
#         else:
#             return 0

#     def top(self):
#         if self.size() != 0:
#             return self.list[-1]
#         else:
#             return -1


# num = int(input())
# stack = Stack()
# while (num > 0):
#     num -= 1
#     input_split = input().split()

#     command = input_split[0]

#     if command == "push":
#         stack.push(input_split[1])
#     elif command == "pop":
#         print(stack.pop())
#     elif command == "size":


# import sys
# input = sys.stdin.readline

# s = []
# n = int(input().rstrip())

# for _ in range(n):
#     op = list(map(str, input().split()))
#     if op[0] == 'push':
#         s.append(int(op[1]))
#     elif op[0] == 'pop':
#         print(s[-1] if len(s) else -1)
#         s = s[:-1]
#     elif op[0] == 'size':
#         print(len(s))
#     elif op[0] == 'empty':
#         print(0 if len(s) else 1)
#     elif op[0] == 'top':
#         print(s[-1] if len(s) else -1)

import sys
stack = []
N = int(sys.stdin.readline())
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'pop':
        if len(stack) > 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif command[0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    else:
        pass
