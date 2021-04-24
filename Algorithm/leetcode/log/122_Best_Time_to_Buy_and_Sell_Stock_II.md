#### [122_Best_Time_to_Buy_and_Sell_Stock_II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)


###### My Solution 1
```python
from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        mystock = prices[0]

        for price in prices:
            if price > mystock:
                result += price - mystock
            mystock = price

        return result
```
> Runtime: 56 ms, faster than 91.25% of Python3 online submissions for Best Time to Buy and Sell Stock II.

> Memory Usage: 15.1 MB, less than 23.06% of Python3 online submissions for Best Time to Buy and Sell Stock II.

