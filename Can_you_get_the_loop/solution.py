def loop_size(node):
    slow = node
    fast = node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            count = 1
            cur = slow.next
            while cur != slow:
                count += 1
                cur = cur.next
            return  count
    return False
