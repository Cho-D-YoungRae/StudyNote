#### [5_Longest_Palindromic_Substring](https://leetcode.com/problems/longest-palindromic-substring/)
> 159 pg


###### My Solution 1

```python
from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""

        for l in range(len(s), 0, -1):
            for i in range(len(s) - l + 1):
                to_comp = s[i : i + l]
                if to_comp == to_comp[::-1]:
                    return to_comp
```
> Runtime: 6940 ms, faster than 13.83% of Python3 online submissions for Longest Palindromic Substring.

> Memory Usage: 14 MB, less than 39.23% of Python3 online submissions for Longest Palindromic Substring.                    

주어지는 문자열의 최대 길이가 1000이었고 완전 탐색이 가능할 정도의 숫자여서 시도해보았다. 역시 속도는 느렸다.


###### 교재 풀이 확인

