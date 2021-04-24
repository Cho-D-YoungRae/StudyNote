#### [147_Insertion_Sort_List](https://leetcode.com/problems/insertion-sort-list/)
> 500pg

###### My Solution 1
```python
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
```

> Runtime: 1972 ms, faster than 29.44% of Python3 online submissions for Insertion Sort List.

> Memory Usage: 16.2 MB, less than 79.73% of Python3 online submissions for Insertion Sort List.



*교재풀이 확인*