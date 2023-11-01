a = int(input())
b = str(input())  # str으로 형변환을 해주지 않으면 b[2]에서 에러가 난다.
# TypeError: 'int' object is not subscriptable

a1 = int(b[2]) * a
a2 = int(b[1]) * a
a3 = int(b[0]) * a
print(a1, a2, a3, a * int(b))
