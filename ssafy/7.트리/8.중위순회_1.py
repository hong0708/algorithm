class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def inorder(node):
    if node.left != None:
        inorder(node.left)
    print(node.tree, end='')
    if node.right != None:
        inorder(node.left)


for t in range(10):
    n = int(input())

    tree = {}
    for i in range(n):
        data, left, right = input().split()
        tree[data] = Node(data, left, right)
    print("#{}".format(t + 1, end=''))
    inorder(1)
    print()
