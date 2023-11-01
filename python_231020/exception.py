def divisor():
    try:
        num = int(input("100을 나누기 위한 정수: "))
        print(100/num)
    except ValueError as e:
        print("숫자 형식으로 작성해주세요", e)
        divisor()
    except ZeroDivisionError as e:
        print("영으로 나눌 수 없습니다.", e)
        divisor()
    except Exception as e:
        print(e, e.__class__)
    finally:
        print("언제 -> try 블록이 정상적으로 실행되는 경우")


divisor()
