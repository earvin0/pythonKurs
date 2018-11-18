class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def remove_head(node):
    if node is None:
        raise ValueError("Pusta lista")

    return node.next, node.data


def remove_tail(node):
    if node is None:
        raise ValueError("Pusta lista")
    elif node.next is None:
        return None, node.data

    current_node = node
    while current_node.next.next is not None:
        current_node = current_node.next

    temp_data = current_node.next.data
    current_node.next = None

    return node, temp_data


head = None
head = Node(4, head)
head = Node(3, head)
head = Node(2, head)
head = Node(1, head)


while head:
    head, node = remove_head(head)
    print("usuwam", node)

head = None
head = Node(4, head)
head = Node(3, head)
head = Node(2, head)
head = Node(1, head)


while head:
    head, node = remove_tail(head)
    print("usuwam", node)

head = None
try:
    remove_head(head)
except ValueError:
    print("zlapano wyjatek")

head = Node(1, None)
print(remove_head(head))
head = Node(None, None)
print(remove_head(head))
