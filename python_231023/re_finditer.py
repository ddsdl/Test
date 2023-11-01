import re

# 알파벳 소문자가 1개 이상 있는 문자열을 체크하는 정규식
# 정규식을 컴파일하고, 컴파일된 객체를 반환(c_re_obj)
c_re_obj = re.compile('[a-z]+')

# 컴파일된 객체를 이용해 finditer 함수를 사용
# finditer 함수 : 매치된 문자열을 반복 가능한 객체(iterator)로 반환
# 여기에 반복가능한 객체는 'match 객체'로 구성되어 있다.
match_lter = c_re_obj.finditer("파이th0n")

print(match_lter)

str = ''
for i in match_lter:
    print(i)
    str += "파이th0n"[i.start():i.end()]

print(str)
