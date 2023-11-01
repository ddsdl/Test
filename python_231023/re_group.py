import re

match_obj = re.search(
    '(\w+)\s+([0,1]{3}[-]\d{4}[-]\d{4})', '홍길동 010-1234-5678')

print(match_obj.group())  # 전체출력
print('----------------')
print(match_obj.group(0))  # 전체출력
print('----------------')
print(match_obj.group(1))  # 첫번째 그룹만 출력 ( 홍길동 )
print('----------------')
print(match_obj.group(2))  # 두번째 그룹만 출력 ( 010-1234-5678 )
print('----------------')
