def get_user_number(start, end):
    user_number = int(input(f"{start} 부터 {end}"))
    if user_number > 30 or user_number < 1:
        raise Exception(f"숫자 범위 초과\n")
    return user_number


def up_down_game():
    import random
    random_number = random.randint(1, 30)
    try:
        while True:
            user_input = get_user_number(1, 30)
            if user_input == random_number:
                print('축하합니다~! 정답입니다!!!')
                break
            # elif user_input > 30 or user_input < 1 :
            #     print('범위 안의 숫자를 입력해주세요\n')
            elif user_input < random_number:
                print('up\n')
            else:
                print('down\n')
    except Exception as e:
        print(e)
        raise Exception("에러 전달")


try:
    up_down_game()
except Exception as e:
    print(e)
