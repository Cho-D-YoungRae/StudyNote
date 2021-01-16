#### [240_Search_a_2D_Matrix_II](https://leetcode.com/problems/valid-anagram/)
> 537pg


###### My Solution 1

```python
from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    break

        return False
```

> Runtime: 184 ms, faster than 16.49% of Python3 online submissions for Search a 2D Matrix II.

> Memory Usage: 20.6 MB, less than 26.12% of Python3 online submissions for Search a 2D Matrix II.

풀긴했으나 이렇게 풀라는 의도가 아니었을 것..
*교재풀이확인*