# [241_Different_Ways_to_Add_Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)



## Try 1 - WRONG

```python
from typing import *


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def calculate(num1: List[int], num2: List[int], op: str) -> List[int]:
            if op == '+':
                operator = lambda x, y : x + y
            elif op == '-':
                operator = lambda x, y : x - y
            elif op == '*':
                operator = lambda x, y : x * y

            result = []
            for x in num1:
                for y in num2:
                    result.append(operator(x, y))

            return result

        def dfs(input: str) -> List[int]:
            if len(input) == 1:
                return [int(input)]

            result = []
            for i in range(1, len(input), 2):
                left = dfs(input[:i])
                right = dfs(input[i+1:])
                result += calculate(left, right, input[i])

            return result

        return dfs(input)
```
> Input
"11"

> Output
[]

> Expected
[11]

숫자를 모두 1자리라고 착각했다.

## 참고
- `파이썬 알고리즘 인터뷰`: 616pg