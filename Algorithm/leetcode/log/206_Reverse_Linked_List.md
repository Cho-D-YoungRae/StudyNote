#### [206_Reverse_Linked_List](https://leetcode.com/problems/reverse-linked-list/)
> 219pg


###### My Solution 1
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        result = None
        
        while head:
            head.next, head, result = result, head.next, head
            
        return result
```

> Runtime: 36 ms, faster than 70.81% of Python3 online submissions for Reverse Linked List.

> Memory Usage: 15.4 MB, less than 7.80% of Python3 online submissions for Reverse Linked List.

###### 교재 재귀 풀이 확인