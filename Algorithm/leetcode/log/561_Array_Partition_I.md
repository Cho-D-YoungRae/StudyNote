#### [561_Array_Partition_I](https://leetcode.com/problems/array-partition-i/)
> 193pg


###### My Solution 1
```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
```

> Runtime: 312 ms, faster than 33.61% of Python3 online submissions for Array Partition I.

> Memory Usage: 16.8 MB, less than 5.06% of Python3 online submissions for Array Partition I.