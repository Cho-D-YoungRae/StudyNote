#### [239_Sliding_Window_Maximum](https://leetcode.com/problems/sliding-window-maximum/)
> 571pg

###### My Solution 1 - 시간초과
```python
from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i+k]))

        return result
```

###### My Solution 2 - timeout
```python
from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        maxinslide = None
        for i in range(len(nums) - k + 1):
            if not maxinslide:
                maxinslide = max(nums[i:i+k])
            else:
                maxinslide = max(maxinslide, nums[i+k-1])

            result.append(maxinslide)
            if maxinslide == nums[i]:
                maxinslide = None

        return result
```

###### My Solution 3
```python
from typing import *
import heapq
from collections import Counter

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        slide_counter = Counter()

        for i in range(k - 1):
            heapq.heappush(heap, -nums[i])
            slide_counter[nums[i]] += 1

        for i in range(k-1, len(nums)):
            heapq.heappush(heap, -nums[i])
            slide_counter[nums[i]] += 1

            maxinslide = -heapq.heappop(heap)
            while slide_counter[maxinslide] == 0:
                maxinslide = -heapq.heappop(heap)

            heapq.heappush(heap, -maxinslide)
            result.append(maxinslide)
            slide_counter[nums[i-k+1]] -= 1

        return result
```

###### 교재풀이 참조

