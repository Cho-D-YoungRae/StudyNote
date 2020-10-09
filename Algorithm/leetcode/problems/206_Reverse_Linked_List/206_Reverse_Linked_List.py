class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        result = None
        
        while head:
            head.next, head, result = result, head.next, head
            
        return result