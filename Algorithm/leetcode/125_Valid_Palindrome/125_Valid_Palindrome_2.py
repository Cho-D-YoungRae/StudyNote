import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        dq = collections.deque()
        for ch in s:
            if ch.isalnum():
                dq.append(ch.lower())

        for _ in range(len(dq)//2):
            if dq.pop() != dq.popleft():
                return False

        return True