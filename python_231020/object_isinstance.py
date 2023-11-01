class Animal:
    def __init__(self):
        self.name = "unnamed"
        self.age = 0


# 자식 클래스에 생성자가 없는 경우에는 자동으로 부모 생성자를 호출합니다.


class Human(Animal):
    def __init__(self):
        self.job = "student"
        super().__init__()


pig = Animal()
choi = Human()

print(isinstance(pig, Animal))  # True
print(isinstance(pig, Human))  # False
print(isinstance(choi, Animal))  # True
print(isinstance(choi, Human))  # True

print(isinstance(choi, object))
