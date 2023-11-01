def hello_names(count=1, *names):
    # names 를 count 만큼 반복해서 출력
    # (키워드 매개변수, 가변 매개변수) -> 테스트용
    
    for name in names:
        print(name * count)


hello_names(3, "손흥민", "이강인")  # => 가능
# hello_names("손흥민", "이강인", 2) => 불가능 count = "손흥민" 불가능!
# hello_names(count=2, "손흥민", "이강인") => 구문에러, 키워드 매개변수 뒤에 가변 매개변수 불가능!!
# hello_names("손흥민", "이강인") => 불가능 count = "손흥민" 불가능!
