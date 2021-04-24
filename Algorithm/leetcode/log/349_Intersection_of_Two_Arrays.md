#### [349_Intersection_of_Two_Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
> 529pg

###### My Solution 1
```python
from typing import *


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

```
> Runtime: 48 ms, faster than 49.47% of Python3 online submissions for Intersection of Two Arrays.

> Memory Usage: 14.2 MB, less than 98.27% of Python3 online submissions for Intersection of Two Arrays.


###### 교재 풀이 확인 3번