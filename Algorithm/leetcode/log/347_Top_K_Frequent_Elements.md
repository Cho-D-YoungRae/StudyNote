#### [347_Top_K_Frequent_Elements](https://leetcode.com/problems/top-k-frequent-elements/)
> 307pg

###### My Solution 1
```python
from typing import *
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]

```
> Runtime: 96 ms, faster than 81.85% of Python3 online submissions for Top K Frequent Elements.

> Memory Usage: 18.3 MB, less than 22.45% of Python3 online submissions for Top K Frequent Elements.


###### 교재 풀이 확인