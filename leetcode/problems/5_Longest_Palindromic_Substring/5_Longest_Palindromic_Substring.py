from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""

        for l in range(len(s), 0, -1):
            for i in range(len(s) - l + 1):
                to_comp = s[i : i + l]
                if to_comp == to_comp[::-1]:
                    return to_comp