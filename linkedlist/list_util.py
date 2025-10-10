class ListNode:

    def __init__(self, value: int):
        self.value = value
        self.next: ListNode = None

    def __str__(self):
        return str(self.value)

class ListUtil:

    @staticmethod
    def create_linked_list(arr)-> ListNode:
        node = ListNode(-1)
        current = node
        for value in arr:
            next_node = ListNode(value)
            current.next = next_node
            current = current.next
        return node.next

    @staticmethod
    def print_linklist(node: ListNode, msg: str = ''):
        current = node
        values = []
        while current:
            values.append(current.value)
            current = current.next
        output = "->".join(str(item) for item in values)
        print(msg, output)
