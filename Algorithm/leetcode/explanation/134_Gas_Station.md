# [134_Gas_Station](https://leetcode.com/problems/insertion-sort-list/)

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

## 참고 풀이
> `파이썬 알고리즘 인터뷰` - 599pg
```python
from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주요소 방문 가능 여부 판별
        if sum(gas) < sum(cost):
            return -1

        # 모든 주유소방문이 가능하다면 출발점 '한 곳 존재'(문제조건)
        # 전체를 방문하며 성립되지 않으면 출발점을 한 칸씩 뒤로 밀어낸다.
        # 정답은 한 곳이므로 이미 지나간 앞부분 다시 확인할 필요 없음
        # 성립하는 곳 찾으면 그 곳이 정답

        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안 되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]

        return start
```
