#### [77_Combinations](https://leetcode.com/problems/combinations/)
> 346pg

###### My Solution 1

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations([num for num in range(1, n+1)], k))
```

> Runtime: 76 ms, faster than 96.03% of Python3 online submissions for Combinations.

> Memory Usage: 15.3 MB, less than 62.84% of Python3 online submissions for Combinations.

###### My Solution 2

```python
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
```

> Runtime: 460 ms, faster than 71.76% of Python3 online submissions for Combinations.

> Memory Usage: 15.4 MB, less than 47.39% of Python3 online submissions for Combinations.