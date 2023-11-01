import re

# 알파벳 소문자가 1개 이상 있는 문자열을 체크하는 정규식
# 정규식을 컴파일하고, 컴파일된 객체를 반환(c_re_obj)
c_re_obj = re.compile('[a-z]+')

# 컴파일된 객체를 이용해 findall 함수를 사용
# findall 함수 : 매치된 문자열을 리스트로 반환한다.
match_list = c_re_obj.findall("파이th0n")

print(type(match_list))
print(match_list)
