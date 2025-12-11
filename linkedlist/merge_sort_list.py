from list_node import ListNode
from list_util import ListUtil

class MergeSort:

    def __middle(self, node: ListNode) -> ListNode:
        slow = node
        fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sort(self, head: ListNode) -> ListNode:
        if head and head.next:
            mid = self.__middle(head)
            right_side = mid.next
            mid.next = None
            left_list = self.sort(head)
            right_list = self.sort(right_side)
            return self.__merge(left_list, right_list)
        return head

    def __merge(self, left_node: ListNode, right_node: ListNode) -> ListNode:
        new_node = ListNode(-1)
        current = new_node
        while left_node and right_node:
            if left_node.val < right_node.val:
                current.next = left_node
                left_node = left_node.next
            else:
                current.next = right_node
                right_node = right_node.next
            current = current.next
        if left_node:
            current.next = left_node
        else:
            current.next = right_node
        return new_node.next


if __name__ == "__main__":
    obj = MergeSort()
    arr = [4,2,1,3]
    head = ListUtil.create_linked_list(arr)
    sorted_head = obj.sort(head)
    ListUtil.print_linked_list(sorted_head, "Sorted List: ")
