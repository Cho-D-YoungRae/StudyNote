#### [78_Subsets](https://leetcode.com/problems/subsets/)
> 355 pg

###### My Solution 1

```python
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
```

> Runtime: 36 ms, faster than 44.78% of Python3 online submissions for Subsets.

> Memory Usage: 14.6 MB, less than 7.69% of Python3 online submissions for Subsets.

###### 교재 코드 참고