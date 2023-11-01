# N = int(input())
# A = list(map(int, input()))

# sum = 0

# for i in range(len(A)):

#     sum = sum + A[i]

# print(sum)

# n = int(input())
# n_str = input()
# result = 0

# for i in n_str:
#     result += int(i)

# print(result)


def sum(n, n_str):
    result = 0
    for i in n_str:
        result += int(i)
    return result


n = int(input())
n_str = input()
