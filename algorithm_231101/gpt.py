class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")


# 이진 트리 생성
root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.left = TreeNode("F")
root.right.right = TreeNode("G")
root.left.left.left = TreeNode("H")

# 후위 순회 실행
postorder_traversal(root)
dsasdasd
