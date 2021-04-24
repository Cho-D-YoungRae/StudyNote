#### [24_Swap_Nodes_in_Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
> 229pg


###### My Solution 1
```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        head.next.next, head.next, head = \
            head, head.next.next, head.next

        head.next.next = self.swapPairs(head.next.next)

        return head
```

> Runtime: 28 ms, faster than 84.91% of Python3 online submissions for Swap Nodes in Pairs.

> Memory Usage: 13.8 MB, less than 99.99% of Python3 online submissions for Swap Nodes in Pairs.

###### 교재 풀이 확인
