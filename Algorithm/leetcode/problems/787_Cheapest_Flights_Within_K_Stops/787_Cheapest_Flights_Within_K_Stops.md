#### [787_Cheapest_Flights_Within_K_Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
> 379pg


###### My Solution 1 - WRONG

``` python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for v, u, w in flights:
            graph[v].append((u, w))

        Q = [(0, -1, src)] # weight, count, start
        dist = defaultdict(list)

        while Q:
            weight, count, node = heapq.heappop(Q)
            dist[node].append((weight, count))
            for u, w in graph[node]:
                alt = weight + w
                heapq.heappush(Q, (alt, count+1, u))

        for weight, count in dist[dst]:
            if count <= K:
                return weight

        return -1
```

> 5
[[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
0
4
1

`Time Limit Exceeded`

종료 조건이 정해져있지 않아서 싸이클이 생길 경우 무한루프