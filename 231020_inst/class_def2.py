# 클래스의 생성
class Animal:
    age = 0
    def set_name(self, data):
        self.name = data

# 클래스를 활용한 객체 생성
pig = Animal()
pig.set_name('돼지') # Animal.set_name(pig, "돼지")
pig.age = 3

panda = Animal()
panda.set_name('푸바오')
panda.age = 10

print(f"pig의 정보 [ 이름: {pig.name}, 나이: {pig.age} ]")
print(f"panda의 정보 [ 이름: {panda.name}, 나이: {panda.age} ]")