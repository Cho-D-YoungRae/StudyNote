from typing import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(subset: List[int], idx):
            if idx == len(nums):
                result.append(subset)
                return

            dfs(subset + [nums[idx]], idx+1)
            dfs(subset, idx+1)

        dfs([], 0)
        return result