#### [121_Best_Time_to_Buy_and_Sell_Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

###### My Solution 1
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        maximum = 0

        for i in range(len(prices)):
            if not stack or stack[-1] > prices[i]:
                stack.append(prices[i])
            else:
                maximum = max(maximum, prices[i] - stack[-1])

        return maximum
```

> Runtime: 60 ms, faster than 87.05% of Python3 online submissions for Best Time to Buy and Sell Stock.

> Memory Usage: 14.8 MB, less than 96.87% of Python3 online submissions for Best Time to Buy and Sell Stock.