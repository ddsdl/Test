import collections

# 없는 키로 조회 했을 경우, 에러를 출력하는 대신에 디폴트 값을 기준으로 생성
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4

# {'A': 5, 'B': 4, 'C': 0})이 생성 되고
print(a)
# 'C': 100 이 추가된다
a['C'] += 100
print('========= defalutdict 적용 =============')
print(a)
