#### [424_Longest_Repeating_Character_Replacement](https://leetcode.com/problems/intersection-of-two-arrays/)
> 580pg

###### My Solution 1
```python
from typing import *
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        result = 0
        left = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            l = right - left + 1

            if l - counts.most_common(1)[0][1] > k:
                counts[s[left]] -= 1
                left += 1
            else:
                result = max(result, l)

        return result

```
> Runtime: 304 ms, faster than 15.68% of Python3 online submissions for Longest Repeating Character Replacement.

> Memory Usage: 14.4 MB, less than 26.78% of Python3 online submissions for Longest Repeating Character Replacement.


###### 교재 풀이 확인 3번