import sys

N = int(input())
N_list = [int(sys.stdin.readline())for i in range(N)]


for i in range(len(N_list)):
    min = i
    for j in range(i+1, len(N_list)):
        if N_list[min] > N_list[j]:
            min = j
    N_list[i], N_list[min] = N_list[min], N_list[i]

for i in N_list:
    print(i)


def selection_sorted(list):
    length = len(list)
    for x in range(length - 1):
        min = x
        for y in range(x + 1, length):
            if list[min] > list[y]:
                min = y
        list[x], list[min] = list[min], list[x]
    return list
