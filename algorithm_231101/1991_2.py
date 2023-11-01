import sys


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 전위순회 : 루트 -> 왼쪽 -> 오른쪽


def preorder(node):
    if node:
        print(node.data, end='')
        preorder(node.left)
        preorder(node.right)

# 중위순회 : 왼쪽 -> 루트 => 오른쪽


def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end='')
        inorder(node.right)

# 후위순회 : 왼쪽 -> 오른쪽 -> 루트


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end='')


N = int(sys.stdin.readline().strip())
tree = {}

for _ in range(N):
    data, left, right = sys.stdin.readline().split()
    tree[data] = Node(data, left, right)

root = tree['A']

preorder(root)
print()
inorder(root)
print()
postorder(root)
