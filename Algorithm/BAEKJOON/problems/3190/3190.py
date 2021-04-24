import collections


if __name__ == '__main__':
    n = int(input())
    k = int(input())

    # 게임 보드 초기화
    board = [[0] * n for _ in range(n)]

    # 사과 위치
    for _ in range(k):
        y, x = map(int, input().split())
        board[y-1][x-1] = 1

    # 뱀의 위치는 2로 표시
    board[0][0] = 2

    # 움직임 정보
    l = int(input())
    snake_move_info = []
    for i in range(l):
        snake_move_info.append(input().split())


    direction = {'D' : 1, 'L' : -1} # 방향 회전을 위해

    # 방향에 따른 움직임 동, 남, 서, 북
    movements = ((0, 1), (1, 0), (0, -1), (-1, 0))

    # 앞으로 나아가고 뒤 부분 줄어드는 뱀 큐의 형태로 구현
    snake = collections.deque()
    snake.append((0,0)) # 첫 위치
    snake_dir = 0   # 첫 방향
    head_y, head_x = 0, 0   # 머리 좌표
    result = 0  # 총 시간
    breaker = False # 반복문 탈출을 위해

    def 
    for t, d in snake_move_info:
        time = int(t)
        time -= result
        for i in range(time):
            # 뱀 움직이고 1초 증가
            y, x = movements[snake_dir]
            head_y += y
            head_x += x
            result += 1
            
            # 벽 혹은 자신에게 부딪히지 않으면
            if 0 <= head_y < n and 0 <= head_x < n and \
                            board[head_y][head_x] != 2:
                # 앞으로 나아간다
                snake.append((head_y, head_x))
            # 부딪히면 종료
            else:
                breaker = True
                break
            
            # 사과를 먹지 않으면
            if board[head_y][head_x] != 1:
                # 꼬리 줄어든다
                y, x = snake.popleft()
                board[y][x] = 0
            
            # 나아간 부분 체크해주기
            board[head_y][head_x] = 2
        
        # 부딪혔을 때 전체 종료
        if breaker : break
        
        # 방향 변경
        snake_dir = (snake_dir + direction[d]) % 4
    
    # 움직임 정보 이외에 아직 부딪히지 않았으면 그 방향으로 계속 나아간다
    while not breaker:
        y, x = movements[snake_dir]
        head_y += y
        head_x += x
        result += 1
        if 0 <= head_y < n and 0 <= head_x < n and \
                board[head_y][head_x] != 2:
            snake.append((head_y, head_x))
        else:
            breaker = True
            break

        if board[head_y][head_x] != 1:
            y, x = snake.popleft()
            board[y][x] = 0

        board[head_y][head_x] = 2


    print(result)