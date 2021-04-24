#### [393_UTF-8_Validation](https://leetcode.com/problems/product-of-array-except-self/)
> 193pg


###### My Solution 1

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 자신을 제외한 곱을 담은 것
        products = [1 for _ in range(len(nums))]
        
        p = 1
        # 앞에서부터 자신보다 앞의 값이 모두 곱해진 값
        for i in range(1, len(nums)):
            p *= nums[i-1]
            products[i] *= p
            
        p = 1
        # 뒤에서부터 자신보다 뒤의 값이 모두 곱해진 값
        for i in range(len(nums)-2, -1, -1):
            p *= nums[i+1]
            products[i] *= p
            
        return products
```

> Runtime: 108 ms, faster than 98.86% of Python3 online submissions for Product of Array Except Self.

> Memory Usage: 20.5 MB, less than 57.08% of Python3 online submissions for Product of Array Except Self.