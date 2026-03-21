class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None':
        return None

    comp = list_repr.split(' -> ')
    index = len(comp) - 2#видалити нан і -1
    node = Node(int(comp[index]), None)

    for i in range(index - 1, -1, -1):
        value = int(comp[i])
        node = Node(value, node)
    return node
