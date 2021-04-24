#### [739_Daily_Temperatures](https://leetcode.com/problems/daily-temperatures/)
> 252pg


###### My Solution 1
```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0 for _ in range(len(T))]
        stack = []

        for today in range(len(T)):
            while stack and T[stack[-1]] < T[today]:
                lastday = stack.pop()
                result[lastday] = today - lastday
            stack.append(today)

        return result
```

> Runtime: 488 ms, faster than 82.78% of Python3 online submissions for Daily Temperatures.

> Memory Usage: 18.4 MB, less than 7.44% of Python3 online submissions for Daily Temperatures.