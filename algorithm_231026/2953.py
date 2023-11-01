# jumsu = [list(map(int, input().split())) for _ in range(5)]
# jumsu_sum = [sum(jumsu[i]) for i in range(5)]
# max_jumsu = max(jumsu_sum)

# print(jumsu_sum.index(max_jumsu)+1, max_jumsu)


jumsu = [sum(list(map(int, input().split()))) for _ in range(5)]
print(jumsu.index(max(jumsu))+1, max(jumsu))
