from typing import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return list(sorted(nums, reverse=True))[k-1]

