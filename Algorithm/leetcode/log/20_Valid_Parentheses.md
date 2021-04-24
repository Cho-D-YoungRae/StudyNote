#### [20_Valid_Parentheses](https://leetcode.com/problems/3sum/)
> 245pg


###### My Solution 1

```python
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(':')', '{':'}', '[':']'}
        stack = []
        for p in s:
            if p in pair:
                stack.append(pair[p])
            else:
                if stack and stack[-1] == p:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0
```

> Runtime: 24 ms, faster than 94.39% of Python3 online submissions for Valid Parentheses.

> Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.