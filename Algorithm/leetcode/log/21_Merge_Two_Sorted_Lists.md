#### [219_Contains_Duplicate_II](https://leetcode.com/problems/contains-duplicate-ii/)
> 213pg


###### My Solution 1
```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = pnode = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                pnode.next, pnode = l1, l1
                l1 = l1.next
            else:
                pnode.next, pnode = l2, l2
                l2 = l2.next
                
        while l1:
            pnode.next, pnode = l1, l1
            l1 = l1.next
        
        while l2:
            pnode.next, pnode = l2, l2
            l2 = l2.next
            
        return result.next
```

> Runtime: 36 ms, faster than 77.38% of Python3 online submissions for Merge Two Sorted Lists.

> Memory Usage: 14 MB, less than 19.66% of Python3 online submissions for Merge Two Sorted Lists.

###### 교재 풀이 확인
