def reverse_list(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

head = reverse_list(node1)

current = head

while current is not None:
    print(current.value, end=" -> ")
    current = current.next

print("None")
