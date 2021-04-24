#### [3_Longest_Substring_Without_Repeating_Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
> 303pg


###### My Solution 1
```python
from typing import *
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        isRepetited = Counter() # set 으로 하는게 더 나을 듯
        toComp = 0
        result = 0
        start = 0

        for end in range(len(s)):
            if not isRepetited[s[end]]:
                isRepetited[s[end]] += 1
                toComp += 1
            else:
                result = max(result, toComp)
                while start < end and s[start] != s[end]:
                    isRepetited[s[start]] -= 1
                    toComp -= 1
                    start += 1

                start += 1
                
        result = max(result, toComp)

        return result


```

> Runtime: 68 ms, faster than 54.13% of Python3 online submissions for Longest Substring Without Repeating Characters.

> Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.


###### 교재 풀이 확인