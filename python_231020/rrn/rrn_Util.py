# 사용자가 정의한 모듈
# data에는 주민번호가 문자열로 들어갑니다.
print("rrn_Util ->", __name__)


def refine_data(data):
    data = data.replace(" ", "").replace("-", "")
    if len(data) != 13:
        return
    return data


def gender(data) -> str:
    gender_digit = int(data[-7])

    if gender_digit == 1 or gender_digit == 3:
        return "남자"
    elif gender_digit == 2 or gender_digit == 4:
        return "여자"
    else:
        return "에러"


def birth(data) -> (int, int, int):
    year_digit = int(data[-7])
    if year_digit == 1 or year_digit == 2:
        year = 1900 + int(data[:2])
    elif year_digit == 3 or year_digit == 4:
        year = 2000 + int(data[:2])

    month = int(data[2:4])
    day = int(data[4:6])

    return year, month, day


if __name__ == "__main__":
    rrn_num = input("주민번호를 입력해주세요\n")
    print(gender(rrn_num))
    print(birth(rrn_num))


# 사용자가 정의한 모듈
# data에는 주민번호(011020-3001313)와 같이 문자열이 들어갑니다.

# def gender(data)-> str:
#     gender_num = int(data[-7])
#     if gender_num % 2 == 0:
#         return "여자"
#     return "남자"

# def birth(data) -> (int, int, int):
#     year = int(data[0:2])
#     month = int(data[2:4])
#     day = int(data[4:6])
#     gender_num = int(data[-7])
#     if gender_num < 3 :
#         year += 1900
#     else :
#         year += 2000
#     return year, month, day

# print(gender(rrn_num))
# print(birth(rrn_num))
