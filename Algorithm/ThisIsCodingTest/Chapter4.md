#### Chapter 04. 구현
###### 상하좌우 (110pg)
python
```python
if __name__ == '__main__':
    # 입력에 따른 이동 방향
    direction_dict = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}

    # 공간의 크기 N * N
    N = int(input())
    # 내 첫 위치
    my_x, my_y = 1, 1

    movements = input().split()

    for movement in movements:
        x, y = direction_dict[movement]
        # 공간을 벗어나지 않으면 이동
        if 1 <= my_x + x <= N and 1 <= my_y + y <= N:
            my_x += x
            my_y += y

    print(my_y, my_x)
```

###### 시각 (113pg) - python \*
**My idear**
0시부터 쭉 시간당 몇 카운트인지 미리 직접 계산 후 더해나가려했다.
그러다보니 실수가 발생

**교재 아이디어**
시, 분, 초 이렇게 3중 반복문을 사용하였다. 3중 반복문이지만 최대 24*60*60 = 86400 이고 이정도는 충분히 돌아갈 수 있다.

###### 2. 왕실의 나이트 (115pg)
python
```python
if __name__ == '__main__':
    my_pos = input()
    # 내 위치 정수화
    my_y, my_x = int(my_pos[1]), (ord(my_pos[0]) - ord('a') + 1)

    # 전체 움직일 수 있는 8가지 경우
    movements = ((2, 1), (2, -1), (-2, 1), (-2, -1),\
                 (1, 2), (1, -2), (-1, 2), (-1, -2))

    result = 0
    for y, x in movements:
        if 1 <= my_y + y <= 8 and 1 <= my_x + x <= 8:
            result += 1

    print(result)
```

###### 3. 게임 개발 (118pg) \*
**첫 풀이 - python**
```python
def is_in_range_pos(y, x, N, M) -> bool:
    return 0 <= y <= N and 0 <= x <= M

if __name__ == '__main__':
    N, M = map(int, input().split())
    my_y, my_x, my_dir = map(int, input().split())
    game_map = []
    for _ in range(N):
        game_map.append(list(map(int, input().split())))

    movements = ((1, 0), (0, 1), (-1, 0), (0, -1))

    result = 0

    while is_in_range_pos(my_y, my_x, N, M)\
                        and not game_map[my_y][my_x]:
        movements_count = 0
        for d in range(1, 5):
            y, x = movements[my_dir - d]
            if is_in_range_pos(my_y+y, my_x+x, N, M)\
                            and not game_map[my_y+y][my_x+x]:
                game_map[my_y][my_x] = 1
                my_y += y
                my_x += x
                movements_count += 1

        if movements_count:
            result += movements_count
        else:
            y, x = movements[my_dir - 2]
            my_y += y
            my_x += x

    print(result)
```
input
> 4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1

output
> 2

오답 요인
1. 문제를 제대로 이해하지 못 했다.
2. 네 방향 모두 이미 가본 칸이거나 바다이면 바라보는 방향의 뒤로 한 칸 이동하게 되는데 이 때 이동하는 칸을 세지 못했다.

**두 번째 풀이**
```python
def is_in_range_pos(y, x, N, M) -> bool:
    return 0 <= y <= N and 0 <= x <= M

if __name__ == '__main__':
    N, M = map(int, input().split())
    my_y, my_x, my_dir = map(int, input().split())
    game_map = []
    for _ in range(N):
        game_map.append(list(map(int, input().split())))

    movements = ((1, 0), (0, 1), (-1, 0), (0, -1))

    game_map[my_y][my_x] = 1
    result = 1

    while is_in_range_pos(my_y, my_x, N, M):
        movements_count = 0
        for d in range(1, 5):
            y, x = movements[my_dir - d]
            if is_in_range_pos(my_y+y, my_x+x, N, M)\
                            and not game_map[my_y+y][my_x+x]:
                game_map[my_y][my_x] = 1
                my_y += y
                my_x += x
                movements_count += 1
                my_dir = (my_dir - d) % 4
                break

        if movements_count:
            result += movements_count
        else:
            y, x = movements[my_dir - 2]
            my_y += y
            my_x += x
            if not game_map[my_y][my_x]:
                result += 1
            break

    print(result)
```
어찌어찌 답은 나오는 것 같다. 깔끔하게 고쳐보자


**My Solution #3** - python
```python
if __name__ == '__main__':
    N, M = map(int, input().split())
    my_y, my_x, my_dir = map(int, input().split())
    game_map = []
    for _ in range(N):
        game_map.append(list(map(int, input().split())))

    # 북 동 남 서 방향으로 이동 할 때
    movements = ((1, 0), (0, 1), (-1, 0), (0, -1))

    # 좌표가 지도의 범위안에 있는지
    def is_in_range_pos(y, x) -> bool:
        return 0 <= y <= N and 0 <= x <= M

    # 첫 시작 위치 다녀갔으니 1로 표시
    # 바다와 마찬가지로 다녀간 곳은 다시 가지 않으니 1로
    game_map[my_y][my_x] = 1
    
    # 시작점을 지나며 시작하므로 1부터
    result = 1

    while True:
        # 이 위치에서 움직였는지 판단하기 위한
        movements_count = 0

        # 왼쪽 방향부터이므로 1부터
        for d in range(1, 5):
            y, x = movements[my_dir - d]

            # 이동하려는 곳이 범위 내에 있고 갈 수 있는 곳
            if is_in_range_pos(my_y+y, my_x+x)\
                and not game_map[my_y+y][my_x+x]:
                my_y += y
                my_x += x
                game_map[my_y][my_x] = 1
                movements_count += 1
                my_dir = (my_dir - d) % 4
                break

        # 움직임이 있었다면 result에 더해준다.
        if movements_count:
            result += movements_count
        # 움직임이 없었다면 -> 네 방향 모두 가본 곳
        else:
            y, x = movements[my_dir-2]
            # 방향을 유지한 채 뒤로 이동할 수 있나
            if is_in_range_pos(my_y+y, my_x+x)\
                and not game_map[my_y+y][my_x+x]:
                my_y += y
                my_x += x
                game_map[my_y][my_x] = 1
                result += 1
            
            # 위로 이동할 수 없으면 끝낸다.
            else:
                break

    print(result)
```    