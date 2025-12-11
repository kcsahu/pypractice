
class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next: ListNode = None

    def get_val(self):
        return self.val

    def __str__(self):
        return str(self.val)

    def __lt__(self, other):
        return self.val < other.val

