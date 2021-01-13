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