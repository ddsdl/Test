from linked_list import LinkedList


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


def main():
    n, k = [int(i) for i in input().split()]
    linked_list = LinkedList(1)
    for i in range(2, n + 1):
        linked_list.append(i)
    result = linked_list.phus(k)
    print("<" + ", ".join(map(str, result)) + ">")


if __name__ == "__main__":
    main()
