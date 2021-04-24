import itertools


if __name__ == '__main__':

    N, M = map(int, input().split())
    house_info = []
    chicken_info = []
    for y in range(N):
        for x, city in enumerate(map(int, input().split())):
            if city == 1:
                house_info.append((y, x))
            if city == 2:
                chicken_info.append((y, x))

    # [집순서[치킨순서]]
    distance_to_chicken = []
    for house in house_info:
        d = []
        for chicken in chicken_info:
            d.append(abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
        distance_to_chicken.append(d)

    answer = float('inf')

    for m_chicken in itertools.combinations(range(len(chicken_info)), M):
        distance = [float('inf') for _ in range(len(house_info))]
        for c in m_chicken:
            for h_idx in range(len(house_info)):
                distance[h_idx] = min(distance[h_idx],
                                      distance_to_chicken[h_idx][c])

        answer = min(answer, sum(distance))

    print(answer)
