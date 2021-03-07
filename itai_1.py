def reverse_linked_list(node):
    prev = None
    current = node
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
a.next = b
b.next = c
reverse_linked_list(a)
print(b.next.data)
print(c.next.data)







