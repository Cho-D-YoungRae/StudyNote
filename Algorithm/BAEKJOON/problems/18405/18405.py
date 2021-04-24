from typing import *
import collections


if __name__ == '__main__':
    n, k = map(int, input().split())

    virus_q = [collections.deque() for _ in range(k+1)]

    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                virus_q[graph[i][j]].append((i, j))

    s, y, x = map(int, input().split())

    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    time = 0

    while virus_q and time < s:
        for i in range(1, k+1):
            for spread_time in range(len(virus_q[i])):
                virus_y, virus_x = virus_q[i].popleft()
                for j in range(4):
                    spread_y, spread_x = virus_y + dy[j], virus_x + dx[j]
                    if 0 <= spread_y < n and 0 <= spread_x < n\
                                and graph[spread_y][spread_x] == 0:
                        graph[spread_y][spread_x] = i
                        virus_q[i].append((spread_y, spread_x))

        time += 1


    print(graph[y-1][x-1])

