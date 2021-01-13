from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        result = ListNode()
        result.next, head = head, head.next
        result.next.next = None

        while head:
            pnode = result
            while pnode.next and head.val >= pnode.next.val:
                pnode = pnode.next
            pnode.next, head.next, head = head, pnode.next, head.next

        return result.next