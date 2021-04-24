#### [207_Course_Schedule](https://leetcode.com/problems/course-schedule/)
> 364pg


###### My Solution 1 - WRONG
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for prev, next in prerequisites:
            graph[prev].append(next)

        is_visited = [False for _ in range(numCourses)]

        def is_cycle_dfs(pre):
            stack = []
            visited_set = set()

            is_visited[pre] = True
            visited_set.add(pre)
            stack.append(pre)
            while stack:
                v = stack.pop()
                for w in graph[v]:
                    if w in visited_set:
                        return True
                    is_visited[pre] = True
                    visited_set.add(w)
                    stack.append(w)

            return False

        for i in range(numCourses):
            if not is_visited[i] and is_cycle_dfs(i):
                return False

        return True

```

> Input:
3
[[0,1],[0,2],[1,2]]

> Output:
false

> Expected:
true

그래프에 싸이클이 존재하는지 확인하는 문제같다.

나의 방식으로 싸이클을 확인하면 위 처럼 선수과목이 두 가지 일 경우 싸이클이 발생한다고 처리할 수 있다.