from bt.tree_node import TreeNode
from bt.treenode_util import TreeNodeUtil
from list_node import ListNode
from list_util import ListUtil


class SortedListBst:

    def __middle(self, head: ListNode, tail: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next != tail and fast.next.next != tail:
            slow = slow.next
            fast = fast.next.next
        return slow

    def __build_tree(self, head: ListNode, tail: ListNode = None) -> TreeNode:
        if head != tail:
            middle = self.__middle(head, tail)
            tnode = TreeNode(middle.val)
            tnode.left = self.__build_tree(head, middle)
            tnode.right = self.__build_tree(middle.next, tail)
            return tnode
        return None

    def sorted_list_bst(self, head: ListNode) -> TreeNode:
        if head:
            root = self.__build_tree(head)
            return root
        return None
if __name__ == '__main__':
    head = ListUtil.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    bst = SortedListBst().sorted_list_bst(head)
    TreeNodeUtil.print_tree(bst, "BST: ")
