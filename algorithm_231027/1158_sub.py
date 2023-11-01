class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def move_next(self, k):
        for _ in range(k):
            self.head = self.head.next

    def josephus(self, n, k):
        if not self.head:
            return []
        result = []
        current = self.head
        while current.next != current:
            self.move_next(k - 1)
            result.append(self.head.data)
            current = self.head
            while current.next.next != self.head:
                current = current.next
            current.next = current.next.next
        return result


def main():
    n, k = map(int, input().split())
    linked_list = LinkedList()
    for i in range(1, n + 1):
        linked_list.append(i)
    result = linked_list.josephus(n, k)
    # 결과를 출력할 때, 정확한 포맷을 맞추기 위해 수정
    output = ", ".join(map(str, result))
    print(f"<{output}>")


if __name__ == "__main__":
    main()
