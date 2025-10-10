from linkedlist.list_util import ListNode, ListUtil

def detect_cycle(head: ListNode)-> bool:
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

def find_middle(head: ListNode)-> ListNode:
    pointer1 = head
    pointer2 = head
    while pointer2.next and pointer2.next.next:
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
    return pointer1

def reverse_list(head: ListNode)-> ListNode:
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def remove_nth_node(head: ListNode, n: int)->ListNode:
    result = ListNode(-1)
    result.next = head
    node1 = result
    node2 = result
    while node1.next:
        node1 = node1.next
        if n > 0:
            n -= 1
        else:
            node2 = node2.next
    if not node1.next and n>0:
        return result.next
    node2.next = node2.next.next
    return result.next


if __name__=="__main__":
    head = ListUtil.create_linked_list([1,2,3,4,5,6,7])
    head = remove_nth_node(head, 2)
    ListUtil.print_linklist(head, "result")
    head = ListUtil.create_linked_list([1,2,3,4,5,6,7])
    head = remove_nth_node(head, 12)
    ListUtil.print_linklist(head, "result")
    head = ListUtil.create_linked_list([1])
    head = remove_nth_node(head, 1)
    ListUtil.print_linklist(head, "Result")
    head = ListUtil.create_linked_list([1,2,3,4,5,6,7])
    mid = find_middle(head)
    print(mid)
    reversed_list = reverse_list(head)
    ListUtil.print_linklist(reversed_list, 'Reversed: ')
