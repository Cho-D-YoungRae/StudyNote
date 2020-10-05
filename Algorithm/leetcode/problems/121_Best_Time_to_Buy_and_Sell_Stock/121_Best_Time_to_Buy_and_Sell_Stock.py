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