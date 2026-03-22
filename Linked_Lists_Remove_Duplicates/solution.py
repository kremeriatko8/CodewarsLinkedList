class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None or head.next is None:
        return head

    cur_node = head
    while cur_node is not None and cur_node.next is not None:
        if cur_node.data == cur_node.next.data:
            cur_node.next = cur_node.next.next
        else:
            cur_node = cur_node.next
    return head
