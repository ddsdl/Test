import sys
pipe = sys.stdin.readline().strip()
stack = []
count = 0  # 잘려진 쇠막대
for i in range(len(pipe)):
    if pipe[i] == "(":
        stack.append(pipe[i])
    else:
        if pipe[i-1] == "(":
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)
