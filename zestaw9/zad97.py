class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def count_leafs(top, suma=0):
    if top is None:
        return 0
    if top.left is None and top.right is None:
        return 1
    return count_leafs(top.left) + count_leafs(top.right)


def calc_total(top):
    if top is None:
        return 0
    return top.data + calc_total(top.left) + calc_total(top.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)
root.right.right.left = Node(9)

print(count_leafs(root))
print(calc_total(root))
