names = input().split()

same = set()
n_same = set()

for name in names:
    if name in n_same:
        same.add(name)
    n_same.add(name)

if same:
    print(same)
else:
    print('none')