from itertools import combinations
from collections import deque




if __name__ == '__main__':
    N, M = map(int, input().split())

    graph = []
    empty_space = []
    birus_start = []
    for i in range(N):
        graph.append(list(map(int, input().split())))
        for j in range(M):
            if graph[i][j] == 0:
                empty_space.append((i, j))
            if graph[i][j] == 2:
                birus_start.append((i, j))

    di = [0, 1, 0, -1]
    dj = [-1, 0, 1, 0]

    def bfs(i, j):
        birusq = deque([(i, j)])
        while birusq:
            birus = birusq.popleft()
            for d in range(4):
                y, x = birus[0]+di[d], birus[1]+dj[d]
                if 0 <= y < N and 0 <= x < M and graph[y][x] == 0:
                    graph[y][x] = 2
                    birusq.append((y, x))



    max_safty = 0

    for walls in combinations(empty_space, 3):
        for wall in walls:
            graph[wall[0]][wall[1]] = 1

        for birus in birus_start:
            bfs(birus[0], birus[1])

        count_safty = 0

        for is_safty in empty_space:
            if graph[is_safty[0]][is_safty[1]] == 0:
                count_safty += 1
            else:
                graph[is_safty[0]][is_safty[1]] = 0

        for wall in walls:
            graph[wall[0]][wall[1]] = 0

        max_safty = max(max_safty, count_safty)



    print(max_safty)
