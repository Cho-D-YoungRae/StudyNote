from typing import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums: List[int]):
            if len(nums) == 1:
                return [[nums[0]]]
            result = []

            for i in range(len(nums)):
                for next in dfs(nums[:i] + nums[i+1:]):
                    result.append([nums[i]]+next)

            return result

        return dfs(nums)