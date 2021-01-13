from typing import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        stack = []

        def dfs(idx, stack_sum):
            if stack_sum == target: # 정렬 후 중복 확인 안 해도 된다.
                result.append(stack[:])
                return

            if stack_sum > target:
                return

            for i in range(idx, len(candidates)):   # idx 부터
                stack.append(candidates[i])
                dfs(i, stack_sum + candidates[i])
                stack.pop()

        dfs(0, 0)

        return result