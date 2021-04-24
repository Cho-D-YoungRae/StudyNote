#### [297_Serialize_and_Deserialize_Binary_Tree](https://leetcode.com/problems/trapping-rain-water/)
> 180 pg


###### My Solution 1 - WRONG

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = deque()
        result = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                top = stack.pop()
                result += height[top] * (i - top - 1)
            stack.append(i)

        return result
```

스택에 인덱스 값을 저장하고 계산할 때 해당 인덱스의 높이를 곱하며 계산한다. 예를 들어 높이 2인 것 앞에 1인 것이 있는 경우 무시되어 계산된다.

