from list_node import ListNode
import heapq
from list_util import ListUtil

def merge_ksorted_list(sorted_list: list)->ListNode:
    pq = []
    for item in sorted_list:
        heapq.heappush(pq, item)
    head = ListNode(-1)
    current = head
    while len(pq) > 0:
        node = heapq.heappop(pq)
        current.next = node
        current = node
        if node.next:
            heapq.heappush(pq, node.next)
    return head.next



if __name__=="__main__":
    list1 = ListUtil.create_linked_list([5,9,12,18])
    list2 = ListUtil.create_linked_list([14,15,18,29,33,51])
    list3 = ListUtil.create_linked_list([1,4,8,21,56])
    list4 = ListUtil.create_linked_list([2,9,12,19,28])
    head = merge_ksorted_list([list1,list2, list3,list4])
    ListUtil.print_linked_list(head, "Sorted list")