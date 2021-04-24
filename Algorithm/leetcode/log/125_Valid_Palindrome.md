#### [125_Valid_Palindrome](https://leetcode.com/problems/valid-palindrome/submissions/)


###### My Solution 1
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.upper())
        result = []
        for ch in s:
            if ch.isalnum():
                result.append(ch)


        return result == result[::-1]
```
>Runtime: 44 ms, faster than 81.44% of Python3 online submissions for Valid Palindrome.

> Memory Usage: 15.9 MB, less than 17.07% of Python3 online submissions for Valid Palindrome.


###### My Solution 2
```python
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
```
> Runtime: 56 ms, faster than 45.23% of Python3 online submissions for Valid Palindrome.

> Memory Usage: 18.8 MB, less than 16.54% of Python3 online submissions for Valid Palindrome.


**re.sub()**
re 모듈을 사용하면 정규식을 이용해 문자열을 다룰 수 있다.
