# N = int(input())
# N_list = []

# for i in range(N):
#     N_list.append(int(input()))

# for i in range(len(N_list)):
#     min = i
#     for j in range(i+1, len(N_list)):
#         if N_list[min] > N_list[j]:
#             min = j
#     N_list[i], N_list[min] = N_list[min], N_list[i]

# for i in N_list:
#     print(i)


# def selection_sorted(list):
#     length = len(list)
#     for x in range(length - 1):
#         min = x
#         for y in range(x + 1, length):
#             if list[min] > list[y]:
#                 min = y
#         list[x], list[min] = list[min], list[x]
#     return list


# print(selection_sorted([5, 4, 2, 6, 3, 1]))

def selection_sort(N_list):
    n = len(N_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if N_list[j] < N_list[min_idx]:
                min_idx = j
        N_list[i], N_list[min_idx] = N_list[min_idx], N_list[i]


n = int(input())
num_list = []

for _ in range(n):
    num = int(input())
    num_list.append(num)

selection_sort(num_list)

for num in num_list:
    print(num)
