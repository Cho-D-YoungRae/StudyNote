from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_val = list(enumerate(nums))
        idx_val.sort(key = lambda x: x[1])

        first, last = 0, len(nums)-1

        while first < last:
            sum_of_nums = idx_val[first][1] + idx_val[last][1]
            if sum_of_nums > target:
                last -= 1
            elif sum_of_nums < target:
                first += 1
            else:
                break

        return [idx_val[first][0], idx_val[last][0]]

