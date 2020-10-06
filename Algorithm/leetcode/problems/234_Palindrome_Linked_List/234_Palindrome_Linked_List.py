class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        toList = []
        
        while head:
            toList.append(head.val)
            head = head.next
            
        return toList == toList[::-1]