def hello1():
    print("안녕하세요")


def hello2(name):
    print("반갑습니다")


def hello3(name, count):
    for i in range(count):
        print("안녕하세요!", name)


hello1()
hello2("여러분 !")
hello3("아침 드셨어요?", 3)


def hello(name='', count=1):
    for _ in range(count):
        print('안녕하세요', name)


hello()
hello("여러분")
hello("아침드셨어요?", 3)
