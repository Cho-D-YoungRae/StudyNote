#### [46_Permutations](https://leetcode.com/problems/permutations/)
> 341 pg


###### My Solution 1
```python
from typing import *
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums, len(nums)))
```

> Runtime: 28 ms, faster than 99.15% of Python3 online submissions for Permutations.

> Memory Usage: 14.4 MB, less than 17.16% of Python3 online submissions for Permutations.


###### My Solution 2
```python
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
```

> Runtime: 40 ms, faster than 62.28% of Python3 online submissions for Permutations.

> Memory Usage: 14.1 MB, less than 88.93% of Python3 online submissions for Permutations.

###### 교재 풀이 확인