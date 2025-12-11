from list_node import ListNode

class ListUtil:

    @staticmethod
    def create_linked_list(arr : list)->ListNode:
        head = ListNode(-1)
        current = head
        for val in arr:
            next_node = ListNode(val)
            current.next = next_node
            current = next_node
        return head.next

    @staticmethod
    def print_linked_list(head: ListNode, message: str = ''):
        current = head
        data = list()
        while current:
            data.append(current.val)
            current = current.next
        data_str = "->".join(str(item) for item in data)
        print(message, data_str)