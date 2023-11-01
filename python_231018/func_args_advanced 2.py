def hello_names(*names, count=1):
    # names 를 count 만큼 반복해서 출력
    # (가변 매개변수, 키워드 매개변수) -> 테스트용
    # 가변 매개변수를 앞에 쓰는게 좋다
    for name in names:
        print(name * count)


hello_names("손흥민", "이강인", count=2)
# hello_names(2, "손흥민", "이강인")  # => 작동은 될 수 있으나, 원하는 동작이 아님!
# hello_names("손흥민", "이강인", 2) # => 작동은 될 수 있으나, 원하는 동작이 아님!
# hello_names(count=2, "손흥민", "이강인") => 구문에러, 키워드 매개변수 뒤에 가변 매개변수 불가능!!
# hello_names("손흥민", "이강인") => 불가능 count = "손흥민" 불가능!
