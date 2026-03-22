class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError()

    first_part = head
    second_part = head.next
    cur_first = first_part
    cur_second = second_part

    cur = head.next.next
    turn = True
    while cur is not None:
        if turn:
            cur_first.next = cur
            cur_first = cur_first.next
        else:
            cur_second.next = cur
            cur_second = cur_second.next

        cur = cur.next
        turn = not turn
    cur_first.next = None
    cur_second.next = None
    return Context(first_part, second_part)
