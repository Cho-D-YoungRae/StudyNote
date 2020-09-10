from typing import *
import heapq


class Solution:
    def reverseString(self, s: List[str]) -> None:
        front, back = 0, len(s) - 1

        while front < len(s)//2:
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1