colors = ["red", "orange", "yellow", "green"]

enum_colos = enumerate(colors)

print(colors)
print(list(enum_colos))

for i, c in range(len(colors)):
    print(i, c)
