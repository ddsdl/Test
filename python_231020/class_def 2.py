# 클래스의 생성
class Animal:
    # 생성자를 통한 객체 초기화
    def __init__(self):
        self.name = "unnamed"
        self.age = 0

    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}")


# 클래스를 활용한 객체 생성
pig = Animal()
pig.name = "꿀꿀이"  # Animal.set_name(pig, "돼지")
pig.age = 5


panda = Animal()
panda.name = "푸바오"
panda.age = 10

print(f"pig의 정보 [이름:{pig.name}, 나이: {pig.age}]")
print(f"panda의 정보 [이름:{panda.name}, 나이: {panda.age}]")
