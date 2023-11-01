input_val = input("이름과 나이를 입력하세요 (예: 홍길동 20) \n")
name, age = input_val.split(" ")
print(name, int(age))