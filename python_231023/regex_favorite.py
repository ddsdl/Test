import re

# 비밀번호 (8자리 이상, 알파벳, 숫자, !@#$%^&*사용 가능)
password = '^[a-zA-Z0-9!@#$%^&*$]{8,}$'


# 이메일
# 아이디@도메인명.알파벳
email = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9$.-]+\.[a-zA-Z]{2,}'

# 전화번호
mobile = '^(01[0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})$'
# IP
ip = '^([0-9]{1,3}\.){3}[0-9]{1,3}$'

# URL
# http/https : 도메인 인증서 존재 여부
# https://naver.com
url = '^https?://[a-zA-Z0-9.-_~]+\.[a-zA-Z]{2,}$'


# 날짜
dot_date = '^([0-9]{4})\.([0-9]{1,2})\.([0-9]{1,2})\.?$'
minus_date = '^([0-9]{4})-([0-9]{1,2})-([0-9]{1,2})?$'
slash_date = '^([0-9]{4})/([0-9]{1,2})/([0-9]{1,2})$'

# 시간
time = '^(\d{2}):(\d{1,2}):(\d{1,2})$'
results = re.findall(time, '11:34:59')
print(results)