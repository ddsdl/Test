# 빈 딕셔너리의 생성

son_info = {} # son_info = dict()

# 딕셔너리 생성
blackpink_info = {
    'member' : ['제니','지수','로제','리사'],
    'company': 'YG',
    'age' : 20
}
# CRUD (CREATE, READ, UPDATE, DELETE)

# key 를 통한 딕셔너리 접근
print(blackpink_info['member'])

# 딕셔너리 수정
blackpink_info['company'] = 'free'
print(blackpink_info)

# 딕셔너리 삭제
blackpink_info['company']
print(blackpink_info)

# 딕셔너리 값 추가
blackpink_info['world_tour'] = ["프랑스","중국","미국","필리핀","일본"]
print(blackpink_info)
