from typing import *
from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        isRepetited = Counter()
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

