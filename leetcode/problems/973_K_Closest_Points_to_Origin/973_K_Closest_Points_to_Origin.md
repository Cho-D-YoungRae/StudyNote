#### [973_K_Closest_Points_to_Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
> 511pg

###### My Solution 1
```python
from typing import *


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points,key=lambda point: point[0]**2 + point[1]**2)[:K]
```

> Runtime: 624 ms, faster than 92.54% of Python3 online submissions for K Closest Points to Origin.

> Memory Usage: 19.5 MB, less than 92.41% of Python3 online submissions for K Closest Points to Origin.