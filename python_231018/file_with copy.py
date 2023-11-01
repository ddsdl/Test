import random
random_n = [random.randint(1, 30) for _ in range(10)]

with open("rand_num10.txt", "w", encoding="utf-8") as f:
    for num in random_n:
        f.write(str(num) + "\n")


while True:
    search_n = int(input())

    with open("rand_num10.txt", "r") as f:
        lines = f.readlines()

    found = False

    for i, line in enumerate(lines, 1):
        num = int(line.strip())
        if num == search_n:
            print(i)
            found = True
            break

    if not found:
        print('-1')
    else:
        break
