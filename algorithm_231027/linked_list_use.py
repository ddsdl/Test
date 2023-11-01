from linked_list import LinkedList

my_ll = LinkedList("가")

my_ll.append("나")
my_ll.append("다")
my_ll.append("라")

print(my_ll.head)  # <linked_list.Node object at 0x00000198B525A4E0>
print('=====================')
print(my_ll.head.data)  # 가
print('=====================')
print(my_ll.head.next)  # <linked_list.Node object at 0x00000198B525A720>
print('=====================')
print(my_ll.head.next.data)  # 나
print('=====================')
print(my_ll.head.next.next)  # <linked_list.Node object at 0x00000198B525A750>
print('=====================')
print(my_ll.head.next.next.data)  # 다

print(f"{my_ll.delete(1)} 삭제")  # "나" 삭제

print(my_ll.head)  # <linked_list.Node object at 0x000001A44014AE40>
print('=====================')
print(my_ll.head.data)  # 가
print('=====================')
print(my_ll.head.next)  # <linked_list.Node object at 0x000001A44014B0B0>
print('=====================')
print(my_ll.head.next.data)  # 다
print('=====================')
print(my_ll.head.next.next)  # <linked_list.Node object at0x000001A44014B0E0>
print('=====================')
print(my_ll.head.next.next.data)  # 라
