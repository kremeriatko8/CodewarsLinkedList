class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    new_head = head.next
    prev = None
    cur = head
    while cur is not None and cur.next is not None:
        first = cur
        second = first.next
        next_pair = second.next

        second.next = first
        first.next = next_pair
        if prev is not None:
            prev.next = second

        prev = first
        cur = next_pair
    return new_head
