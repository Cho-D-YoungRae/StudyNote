# [406_Queue_Reconstruction_by_Height](https://leetcode.com/problems/queue-reconstruction-by-height/)

## 참조풀이
> `파이썬 알고리즘 인터뷰` - 593pg
```python
from typing import *
import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        # 키 역순, 인덱스 삽입
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        # 키 역순, 인덱스 추출
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
            
        return result
```

패턴을 찾아야 되는 문제이다.

입력 예시가 [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]로 주어졌을 때
```
[[7, 0]] (0번째 인덱스에 [7, 0] 삽입)
[[7,0], [7,1]] (1번째 인덱스에 [7, 1] 삽입)
[[7,0], [6, 1], [7,1]] (1번째 인덱스에 [6, 1] 삽입)
[[5, 0], [7,0], [6, 1], [7,1]] (0번째 인덱스에 [5, 0] 삽입)
[[5, 0], [7,0], [5, 2], [6, 1], [7,1]] (2번째 인덱스에 [5, 2] 삽입)
[[5, 0], [7,0], [5, 2], [6, 1], [4, 4],[7,1]] (4번째 인덱스에 [4, 4] 삽입)
```
- (-[0], [1]) 순서로 삽입이 이루어 진다 
- [1]의 값의 인덱스로 삽입된다.



