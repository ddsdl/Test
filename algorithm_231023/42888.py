# 오픈채팅방
# URL : https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 풀이 시작 : 2023-10-23
# 풀이 완료 :

# def solution(record):
#     user_info = {}
#     answer = []

#     for entry in record:
#         split_entry = entry.split()

#         if split_entry[0] in ["Enter", "Change"]:
#             user_info[split_entry[1]] = split_entry[2]

#         if split_entry[0] == "Enter":
#            answer.append(f"{split_entry[1]}님이 들어왔습니다.")
#         elif split_entry[0] == "Leave":
#            answer.append(f"{split_entry[1]}님이 나갔습니다.")

#     answer = [f"{user_info[answer.split()[0]]}{answer[1:]}"] for answer in answer]

# def solution(record):
#     user_info = {}
#     answer = []
#     for i, user in enumerate(record):
#         user = user.split()
#         if user[1] not in user_info.keys():
#             user_info[user[1]] = [user[2], (i, '님이 들어왔습니다.')]
#         else:
#             if user[0] == 'Enter':

def solution(record):
    answer = []
    user_info = {}

    for i in record:
        r = i.split()
        if r[0] == 'Enter':  # E + 아이디 저장
            answer.append('E' + r[1])
            user_info[r[1]] = r[2]
        elif r[0] == 'Leave':  # L + 아이디 저장
            answer.append('L' + r[1])
        elif r[0] == 'Change':
            user_info[r[1]] = r[2]

    for i in range(len(answer)):  # 딕셔너리 접근하여 출력
        if answer[i][0] == 'E':
            answer[i] = user_info[answer[i][1:]] + '님이 들어왔습니다.'
        else:
            answer[i] = user_info[answer[i][1:]] + '님이 나갔습니다.'

    return answer


record = [
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]

# 결과 출력
answer = solution(record)
for i in answer:
    print(i)

# def solution(record):

#     ans_ = []
#     user_info = {}
#     for record_ in record:
#         cc = record_.split()
#         ans_.append(cc)
#         try:
#             user_info[cc[1]] = cc[2]
#         except:
#             continue

#     answer = []
#     for ans__ in ans_:
#         if 'Enter' in ans__:
#             comment = '님이 들어왔습니다.'

#         if 'Leave' in ans__:
#             comment = '님이 나갔습니다.'

#         if ans__[0] != 'Change':
#             answer.append(user_info[ans__[1]]+comment)

#     return answer


# record = [
#     "Enter uid1234 Muzi",
#     "Enter uid4567 Prodo",
#     "Leave uid1234",
#     "Enter uid1234 Prodo",
#     "Change uid4567 Ryan"
# ]

# # 결과 출력
# answer = solution(record)

# for i in answer:
#     print(i)
