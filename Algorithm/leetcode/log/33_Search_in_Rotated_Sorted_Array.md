#### [33_Search_in_Rotated_Sorted_Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
> 525pg


###### My Solution 1 - WRONG
```python
from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minidx = nums.index(min(nums))

        def binary_search(start, end):
            mid = (start + end)//2
            if start > end:
                return -1

            if nums[mid] < target:
                return binary_search(mid+1, end)
            elif nums[mid] > target:
                return binary_search(start, mid-1)
            else:
                return mid

        if nums[0] < target:
            return binary_search(0, minidx - 1)
        else:
            return binary_search(minidx, len(nums) - 1)
```

> Input
[1,3]
3

> Output
-1

> Expected
1

가장 작은 원소가 있는 인덱스를 기준으로 나눠서 target 값이 리스트의 첫 원소보다 크면 큰값들이 있는 부분에서 이진탐색, 작으면 작은 값들이 있는부분에서 이진탐색 하려했다.

제대로 정렬되어있는 경우 제대로 작동하지 않음

조건을 잘못 나눈 것 같다


###### 교재 풀이 확인
