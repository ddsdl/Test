N,X = [int(i) for i in input().split()]

A = [int(i) for i in input().split()]

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")