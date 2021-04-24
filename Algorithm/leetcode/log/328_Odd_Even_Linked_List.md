#### [328_Odd_Even_Linked_List](https://leetcode.com/problems/odd-even-linked-list/)
> 233pg


###### My Solution 1

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head and head.next:
            odd, even = head, head.next
            evenhead = head.next

            p = even.next
            while p and p.next:
                odd.next, odd, p = p, p, p.next
                even.next, even, p = p, p, p.next

            if p:
                odd.next, odd, p = p, p, p.next
                even.next = None

            odd.next = evenhead


        return head
```

> Runtime: 44 ms, faster than 68.20% of Python3 online submissions for Odd Even Linked List.

> Memory Usage: 15.8 MB, less than 5.40% of Python3 online submissions for Odd Even Linked List.


###### 교재 풀이 확인