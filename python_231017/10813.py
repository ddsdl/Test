basket_count,change_count = [int(i) for i in input().split()]

baskets = [i for i in range(1, basket_count+1)]
for i in range(change_count):
    start, end = [int(i) for i in input().split()]
    baskets[start-1],baskets[end-1] = baskets[end-1],baskets[start-1]
    
print(*baskets)