#### [316_Remove_Duplicate_Letters](https://leetcode.com/problems/remove-duplicate-letters/)
> 247pg


###### My Solution 1 -> WRONG

```python
from typing import *
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        scount = Counter(s)
        stack = []

        for c in s:
            while stack and scount[stack[-1]] and ord(stack[-1]) >= ord(c):
                stack.pop()

            stack.append(c)
            scount[c] -= 1

        return ''.join(stack)
```

> 중복된 문자 처리 못 함
