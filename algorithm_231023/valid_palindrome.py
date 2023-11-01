# 팰린드롬 확인하기
# URL : https://leetcode.com/problems/valid-palindrome/
# 풀이 시작 : 2023-10-23
# 풀이 완료 : 2023-10-23

def is_palindrome(s: str) -> bool:

    strs = [i for i in s.lower() if i.isalnum()]
    a, b = 0, len(strs) - 1
    while a < b:
        if strs[a] != strs[b]:
            return False
        a += 1
        b -= 2
    return True


str = input()
result = is_palindrome(str)

if result:
    print("true")
else:
    print("false")
