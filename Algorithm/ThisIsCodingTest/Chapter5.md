#### Chapter 04. DFS/BFS

###### 3. 음료수 얼려먹기 (149pg)
python
```python
if __name__ == '__main__':

    N, M = map(int, input().split())

    mold = []
    for _ in range(N):
        mold.append(list(map(int, list(input()))))

    def dfs(y, x):
        mold[y][x] = 1
        if y + 1 < N and mold[y+1][x] == 0:
            dfs(y + 1, x)
        if y -1 >= 0 and mold[y-1][x] == 0:
            dfs(y - 1, x)
        if x + 1 < M and mold[y][x+1] == 0:
            dfs(y, x+1)
        if x - 1 >= 0 and mold[y][x-1] == 0:
            dfs(y, x-1)


    result = 0
    for i in range(N):
        for j in range(M):
            if mold[i][j] == 0:
                dfs(i, j)
                result += 1

    print(result)
```    

###### 4. 미로 탈출 (152pg)
python
```python
result = float('inf')

if __name__ == '__main__':

    N, M = map(int, input().split())

    graph = []
    for i in range(N):
        graph.append(list(map(int, list(input()))))



    def dfs(y, x, d):
        if not(0 <= y < N and 0 <= x < M) \
                                or graph[y][x] == 0:
            return

        global result
        graph[y][x] = 0

        if y == N-1 and x == M-1:
            result = min(result, d)
        else:
            dfs(y + 1, x, d + 1)
            dfs(y - 1, x, d + 1)
            dfs(y, x + 1, d + 1)
            dfs(y, x - 1, d + 1)

        graph[y][x] = 1


    dfs(0, 0, 1)


    print(result)
```    

최단경로 -> bfs가 유리