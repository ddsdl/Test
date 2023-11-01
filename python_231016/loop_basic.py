for _ in range(5):
    print("홍길동 - for")

x = 0
while x < 5:
    print('홍길동 - while')
    x += 1
    
# range(처음, 끝, 단계)

# 테스트
print(list(range(10)))
print(list(range(1, 10+1)))
print(list(range(1, 10+1, 3)))

# [위험!]무한 루프
# while True:
#     print("무한반복")

sum = 0
for x in range(1, 100+1):
    sum = sum + x
print(sum)

# while 응용 - 업앤다운 숫자맞추기
import random
random_number = random.randint(1, 30)

while True:
    user_input = int(input("맞춰보세요"))
    if user_input < random_number:
        print('UP')
    elif user_input > random_number:
        print('Down')
    else:
        print('정답') 
        break