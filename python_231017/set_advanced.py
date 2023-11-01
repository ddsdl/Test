
s_num1 = set([1, 2, 3, 4, 5, 6])
s_num2 = set([4, 5, 6, 7, 8 ,9])

# 합집합 구하는 방법 3가지
# 1) 세트1 & 세트2 -> 세트1과 세트2의 교집합 반환
print(f"교집합 : {s_num1 & s_num2}")
# 2) 세트1.intersection(세트2) -> 세트1과 세트2의 교집합 반환 
print(f"교집합 : {s_num1.intersection(s_num2)}")
# 3) 세트1.intersection_update(세트2) -> 세트1과 세트2의 교집합 결과를 세트1에 업데이트
s_num1.intersection_update(s_num2)


# ------------------------------------------
s_num1 = set([1, 2, 3, 4, 5, 6])
s_num2 = set([4, 5, 6, 7, 8 ,9])

# 교집합 구하는 방법 3가지
# 1)  세트1 & 세트2 -> 세트 1과 세트2의 교집합 반환
print(f"합집합 : {s_num1 & s_num2}")

# 2)  세트1.intersection(세트2) -> 세트 1과 세트2의 교집합 반환
print(f"합집합 : {s_num1.intersection(s_num2)}")

# 3) 세트1.intersection_update(세트2) -> 세트1과 세트2의 교집합 결과를 세트1에 업데이트
s_num1.intersection_update(s_num2)

# --------------------------------------------

s_num1 = set([1, 2, 3, 4, 5, 6])
s_num2 = set([4, 5, 6, 7, 8 ,9])

# 차집합 구하는 방법 3가지
# 1) 세트1 - 세트2 -> 세트1과 세트2의 차집합 반환
print(f"차집합 : {s_num1 - s_num2}")
# 2) 세트1.difference(세트2) -> 세트1과 세트2의 차집합 반환
print(f"차집합 : {s_num1.difference(s_num2)}")
# 3) 세트1.difference_update(세트2) -> 세트1과 세트2의 차집합 결과를 세트1에 업데이트
s_num1.difference_update(s_num2)

# ------------------------------------------------

# 대차집합 구하는 방법 3가지
# 1) 세트1 ^ 세트2 -> 세트1과 세트2의 대차집합 반환
print(f"대차집합 : {s_num1 ^ s_num2}")
# 2) 세트1.difference(세트2) -> 세트1과 세트2의 대차집합 반환
print(f"대차집합 : {s_num1.difference(s_num2)}")
# 3) 세트1.difference_update(세트2) -> 세트1과 세트2의 대차집합 결과를 세트1에 업데이트
s_num1.difference_update(s_num2)