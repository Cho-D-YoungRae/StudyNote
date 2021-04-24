from itertools import permutations

def baek_sol():
    N = int(input())
    A = list(map(int, input().split()))
    op_list = [] # 0: +, 1: -, 2: *, 3: /
    max_answer = float('-inf')
    min_answer = float('inf')

    for i, v in enumerate(input().split()): # 연산자 종류, 개수
        op_list += [i for _ in range(int(v))]

    for op_per in permutations(op_list, len(op_list)):
        result = A[0]
        for i in range(len(op_per)):
            if op_per[i] == 0:
                result += A[i + 1]
            elif op_per[i] == 1:
                result -= A[i + 1]
            elif op_per[i] == 2:
                result *= A[i + 1]
            elif op_per[i] == 3:
                minus = False
                if result < 0:
                    minus = True
                    result *= -1

                result //= A[i + 1]
                if minus:
                    result *= -1


        max_answer = max(max_answer, result)
        min_answer = min(min_answer, result)


    print(max_answer)
    print(min_answer)