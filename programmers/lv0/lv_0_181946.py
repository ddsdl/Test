# 문자열 붙여서 출력하기
# URL : https://school.programmers.co.kr/learn/courses/30/lessons/181946
# 풀이 시작 : 2023-10-19
# 풀이 완료 : 2023-10-19

str1, str2 = input().strip().split(' ')
print(f'{str1}{str2}')
# str1, str2 = input().strip().split(' ')
# print(str1, str2, sep='')

# sep=" "
# 이 옵션을 이용하게 되면
# print문의 출력문들 사이에 해당하는 내용을 넣을 수 있습니다.
# 기본 값으로는 공백이 들어가 있으며 이를 사용해 원하는 문자를 입력할 수 있습니다.
