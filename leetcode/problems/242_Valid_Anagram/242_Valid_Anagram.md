#### [242_Valid_Anagram](https://leetcode.com/problems/valid-anagram/)
> 507pg


###### My Solution 1

```python
from typing import *
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
```

> Runtime: 40 ms, faster than 88.42% of Python3 online submissions for Valid Anagram.

> Memory Usage: 14.5 MB, less than 46.52% of Python3 online submissions for Valid Anagram.