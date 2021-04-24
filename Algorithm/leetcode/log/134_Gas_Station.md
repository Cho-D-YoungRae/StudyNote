# [134_Gas_Station](https://leetcode.com/problems/insertion-sort-list/)
> 599pg

## Try 1
```python
from typing import *
import heapq


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 가스 합이 비용 합보다 적으면 한바퀴 돌 수 없다.
        if sum(gas) < sum(cost):
            return -1

        # (가스 - 비용)의 역순으로 저장
        heap = []
        for i in range(len(gas)):
            heapq.heappush(heap, (-(gas[i]-cost[i]), i))

        while heap:
            # (가스 - 비용)이 가장 큰 곳부터 시작점으로 잡는다.
            rest_gas, start = heapq.heappop(heap)
            rest_gas *= -1
            # 그 시작점부터 한바퀴 돌 수 있는지 확인
            for i in range(1, len(gas)):
                curIdx = (start + i) % len(gas)
                rest_gas += gas[curIdx] - cost[curIdx]
                if rest_gas < 0:
                    break
            if rest_gas >= 0:
                return start

        return -1
```

> Runtime: 4432 ms, faster than 8.41% of Python3 online submissions for Gas Station.

> Memory Usage: 16.2 MB, less than 5.39% of Python3 online submissions for Gas Station.