# For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    new_node = Node(data)

    if head is None or data < head.data:
        new_node.next = head
        return new_node

    cur_node = head
    while cur_node.next is not None and data > cur_node.next.data:
        cur_node = cur_node.next

    new_node.next = cur_node.next
    cur_node.next = new_node
    return head
