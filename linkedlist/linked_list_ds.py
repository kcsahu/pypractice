from list_node import ListNode
from list_util import ListUtil


def build_print_linked_list():
    arr = [1, 2, 3, 4, 5, 6, 7]
    head = ListUtil.create_linked_list(arr)
    ListUtil.print_linked_list(head, "LinkedList: ")


def reverse_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev


def middle_node(head: ListNode) -> ListNode:
    fast, slow = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def detect_cycle(head: ListNode) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


### 1->2->3->4->5->6, 2 => 1->2->3->4->6
def remove_nth_node(head: ListNode, n: int):
    node1, node2 = head, head
    while node1.next:
        node1 = node1.next
        if n > 0:
            n -= 1
        else:
            node2 = node2.next
    node2.next = node2.next.next


### 1->2->3->4->5->6, 2 => 5->6->1->2->3->4
def rotate_right(head: ListNode, k: int) -> ListNode:
    if k == 0:
        return head
    size = 0
    node1 = head
    while node1:
        size += 1
        node1 = node1.next
    k = k % size
    if k == 0:
        return head
    node1, node2 = head, head
    while node1.next:
        node1 = node1.next
        if k > 0:
            k -= 1
        else:
            node2 = node2.next
    new_head = node2.next
    node2.next = None
    node1.next = head
    return new_head


if __name__ == "__main__":
    build_print_linked_list()
    ### Reverse a list:
    head = ListUtil.create_linked_list([1,2,3,4,5])
    ListUtil.print_linked_list(head, "Original List: ")
    head = reverse_list(head)
    ListUtil.print_linked_list(head, "Reversed List")
    ### Middle Node
    head = ListUtil.create_linked_list([1,2,3])
    middle = middle_node(head)
    print(middle.val)
    ## Remove nth Node from end of the list
    head = ListUtil.create_linked_list([1, 2, 3, 4, 5, 6])
    remove_nth_node(head, 4)
    ListUtil.print_linked_list(head, "Result: ")
    ## Rotate Right
    head = ListUtil.create_linked_list([1, 2, 3, 4, 5, 6])
    new_head = rotate_right(head, 2)
    ListUtil.print_linked_list(new_head, "Rotated: ")
