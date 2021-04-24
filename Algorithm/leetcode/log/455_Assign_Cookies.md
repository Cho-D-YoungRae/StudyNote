# [455_Assign_Cookies](https://leetcode.com/problems/diameter-of-binary-tree/)
> 603pg

## Try 1
```python
from typing import *
import heapq


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g, s 오름차순으로
        heapq.heapify(g)
        heapq.heapify(s)

        result = 0
        while g and s:
            # 오름차순된 g, s에서 하나씩 꺼낸다.
            greed, cookie_size = heapq.heappop(g), heapq.heappop(s)
            # greed 가 cookie_size 보다 더 크면 조건 만족할 때까지 쿠키 꺼낸다
            # greed는 오름차순 정렬되어 있으므로 조건을 만족하지 못하는 쿠키는
            # 다른 아이에게 갈 수 없다.
            while s and greed > cookie_size:
                cookie_size = heapq.heappop(s)
            
            if greed <= cookie_size:
                result += 1

        return result
```
> Runtime: 312 ms, faster than 10.70% of Python3 online submissions for Assign Cookies.

> Memory Usage: 15.9 MB, less than 82.77% of Python3 online submissions for Assign Cookies.

힙을 사용하는 것 보다 `g`, `s` 리스트를 정렬하고 인덱스를 한 칸씩 이동하면서 하는 것이 더 빠르다. -> 교재풀이


