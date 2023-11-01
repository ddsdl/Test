print(f"object {dir(object)}")


class Book:
    pass


# 사용자 정의 클래스가 가진 속성들
print(dir(Book))

# 사용자 정의 클래스만이 가진 속성들
print(set(dir(Book)) - set(dir(object)))


# 사용자 정의 클래스가 object의 모든 속성을 가지고 있을까?
common_dir = set(dir(Book)).intersection(set(dir(object)))
object_dir = set(dir(object))
print(common_dir == object_dir)  # True
