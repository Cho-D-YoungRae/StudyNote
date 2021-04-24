#### [39_Combination_Sum](https://leetcode.com/problems/combination-sum/)
> 351pg


###### My Solution 1
```python
from typing import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        stack = []

        def dfs(stack_sum):
            if stack_sum == target:
                comb = sorted(stack)
                if comb not in result:
                    result.append(comb)
                return

            if stack_sum > target:
                return

            for i in range(len(candidates)):
                stack.append(candidates[i])
                dfs(stack_sum + candidates[i])
                stack.pop()

        dfs(0)

        return result


```

> Runtime: 644 ms, faster than 5.01% of Python3 online submissions for Combination Sum.

> Memory Usage: 14.2 MB, less than 24.74% of Python3 online submissions for Combination Sum.

###### My Solution 2
```python
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
```
> 1번풀이에서 조금의 수정으로 큰 폭의 성능 향상이 있었다. 1번풀이는 계속 candidates의 처음부터 끝까지 탐색했고, 그러다 보니 중복이 발생하여 중복확인을 하는 작업이 필요했다. 위처럼 idx를 지정해 candidates에서 idx 이전 값은 탐색하지 않아도 된다. 이렇게 하면 중복확인도 안 해도 된다.

> Runtime: 84 ms, faster than 58.47% of Python3 online submissions for Combination Sum.

> Memory Usage: 14.3 MB, less than 24.74% of Python3 online submissions for Combination Sum.

###### 교재 풀이 확인
