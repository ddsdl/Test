# 세트의 함수
s_app = set()
# 세트.add(요소) -> 세트에 새로운 요소를 추가 (이미 존재하는 요소는 넣지 않음)
s_app.add("kakaoTalk")
s_app.add("LINE")

# 세트.update(세트2) -> 세트에 다른 세트를 추가 (이미 존재하는 요소는 넣지 않음)
s_app.update(set(["toss","Netflix","Youtube","Disney+"]))
print(s_app)

# 세트.pop() -> 임의의 요소를 꺼내기
popped_item = s_app.pop()
print(s_app, popped_item)

# 세트.remove(요소) => 세트 내의 특정 요소를 제거 (없는 경우 KeyError)
s_app.remove("Youtube")
print(s_app)

# 세트.discard(요소) => 세트 내의 특정 요소를 제거 (없는 경우, 변경 없음)
s_app.discard("toss")
print(s_app)

# copy
s_app1 = s_app.copy()
print(s_app)
print(s_app1)


# 세트.clear() = 세트의 모든 요소를 제거
s_app1.clear()
print(s_app1)

s_ott_app = set(['Netflix', 'Disney+','Youtube'])
# 세트.isdisjoint(세트2) -> 세트2와의 교집합 존재 여부 반환 ( 존재 시 false)
print(s_app.isdisjoint(s_ott_app))

# 세트.issubset(세트2) -> 세트 2와의 부분집합 관계 여부
print(s_app.issubset(s_ott_app))

# 세트.issuperset(세트2) ->

# len
# element in set