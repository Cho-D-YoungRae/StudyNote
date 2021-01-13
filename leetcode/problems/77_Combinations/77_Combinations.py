from typing import *

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n + 1)]
        result = []
        s = []

        def dfs(idx):
            if len(s) == k:
                result.append(s[:])
                return

            if idx >= n:
                return

            for i in range(idx, n):
                s.append(nums[i])
                dfs(i+1)
                s.pop()

        dfs(0)
        return result