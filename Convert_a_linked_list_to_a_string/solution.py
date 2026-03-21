class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    if not isinstance(node, Node):
        return 'None'

    answer = []
    currentnode = node
    while currentnode is not None:
        answer.append(str(currentnode.data))
        currentnode = currentnode.next
    answer.append('None')
    return ' -> '.join(answer)
