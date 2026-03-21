class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    cur_node = node
    count = 0
    while cur_node is not None:
        if count == index:
            return cur_node
        count += 1
        cur_node = cur_node.next
    raise IndexError()
