#### [215_Kth_Largest_Element_in_an_Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
> 456pg


###### My Solution 1 - WRONG
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return list(sorted(nums, reverse=True))[k-1]
```

> Runtime: 92 ms, faster than 22.98% of Python3 online submissions for Kth Largest Element in an Array.

> Memory Usage: 15.2 MB, less than 41.83% of Python3 online submissions for Kth Largest Element in an Array.



