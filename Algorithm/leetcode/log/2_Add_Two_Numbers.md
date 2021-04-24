#### [2_Add_Two_Numbers](https://leetcode.com/problems/add-two-numbers/)
> 221pg


###### My Solution 1
```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = pnode = ListNode()

        while l1 and l2:
            if not pnode.next:
                pnode.next = ListNode()

            pnode = pnode.next
            pnode.val = pnode.val + l1.val + l2.val
            if pnode.val > 9:
                pnode.val %= 10
                pnode.next = ListNode(1)

            l1, l2 = l1.next, l2.next

        while l1:
            if not pnode.next:
                pnode.next = ListNode()

            pnode = pnode.next
            pnode.val = pnode.val + l1.val
            if pnode.val > 9:
                pnode.val %= 10
                pnode.next = ListNode(1)

            l1 = l1.next

        while l2:
            if not pnode.next:
                pnode.next = ListNode()

            pnode = pnode.next
            pnode.val = pnode.val + l2.val
            if pnode.val > 9:
                pnode.val %= 10
                pnode.next = ListNode(1)

            l2 = l2.next

        return result.next
```

> Runtime: 64 ms, faster than 94.92% of Python3 online submissions for Add Two Numbers.

> Memory Usage: 14.1 MB, less than 99.98% of Python3 online submissions for Add Two Numbers.