#### [771_Jewels_and_Stones](https://leetcode.com/problems/jewels-and-stones/)
> 298pg


###### My Solution 1
```python
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        SCounter = Counter(S)

        result = 0
        for jewel in J:
            result += SCounter[jewel]

        return result
```

> Runtime: 32 ms, faster than 52.75% of Python3 online submissions for Jewels and Stones.

> Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.

###### 교재 4. '파이썬다운 방식' 확인