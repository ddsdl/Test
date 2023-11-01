practice_list = [1, 2, 3, '파이', 'Apple', ['가', '나', '다', '라']]

# 파이를 3.14로 수정
practice_list[3] = 3.14 
print(practice_list)

# 3을 4,8로 수정
practice_list[2] = [4, 8]
print(practice_list)

practice_list[2:3] = [4, 8]

# 리스트의 삭제
print(practice_list)

del practice_list[5]

print(practice_list)

# 라 제거
del practice_list[-1][-1:]
print(practice_list)

# 나 다 삭제
practice_list[-1][1:] = []
print(practice_list)