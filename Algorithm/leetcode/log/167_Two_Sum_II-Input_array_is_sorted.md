#### [167_Two_Sum_II-Input_array_is_sorted](https://leetcode.com/problems/insertion-sort-list/)
> 532pg

###### My Solution 1
```python
from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        front, back = 0, len(numbers) - 1
        while front < back:
            two_sum = numbers[front] + numbers[back]
            if two_sum > target:
                back -= 1
            elif two_sum < target:
                front += 1
            else:
                return [front+1, back+1]
```

> Runtime: 56 ms, faster than 95.49% of Python3 online submissions for Two Sum II - Input array is sorted.

> Memory Usage: 14.7 MB, less than 30.83% of Python3 online submissions for Two Sum II - Input array is sorted.

