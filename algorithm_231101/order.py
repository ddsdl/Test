import sys

N = int(sys.stdin.readline().rstrip())
tree = {}


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# 전위순회 : 루트 -> 왼쪽 -> 오른쪽


def preorder(node):
    print(node.item, end=' ')
    if node.left != ".":
        preorder(tree[node.left])
    if node.right:
        preorder(tree[node.right])


preorder(tree["A"])
# 중위순회 : 왼쪽 -> 루트 => 오른쪽


def inorder(node):
    if node.left != ".":
        inorder(tree[node.left])
    print(node.item, end=' ')
    if node.right:
        inorder(tree[node.right])


inorder(tree["A"])

# 후위순회 : 왼쪽 -> 오른쪽 -> 루트


def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.item, end=' ')

postorder(tree["A"])


for i in range(N):
    data, left, right = sys.stdin.readline().split()
    if left == '.':
        left = None
    if right == '.':
        right = None
    tree[data] = Node(data, left, right)
