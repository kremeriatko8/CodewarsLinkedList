class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    if head == None:
        return Node(data)
    new_head = Node(data)
    new_head.next = head
    return new_head

def build_one_two_three():
    head = None
    for i in range(3, 0, -1):
        head = push(head, i)
    return head
