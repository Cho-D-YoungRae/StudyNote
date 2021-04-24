#### Chapter 11. 그리디 문제

###### 1. 모험가 길드 (311pg)
```python
if __name__ == '__main__':
    N = int(input())
    fear_scale = list(map(int, input().split()))
    
    # 공포도를 내림차순으로 정렬한다
    fear_scale.sort(reverse=True)

    result = 0  # 총 몇 개의 그룹이 생성되었는지
    idx = 0

    
    while idx < N:
        # 현재 idx번째 사람의 공포도 만큼 그룹을 생성하였을 때
        # 사람이 부족함 없이 생성이 가능하면 한 그룹을 생성한다
        if idx + fear_scale[idx] - 1 < N:
            idx += fear_scale[idx] - 1
            result += 1
        
        # 그룹 생성이 불가능 할 경우 그냥 idx 증가
        # 이는 그 전 그룹에 이 사람이 포함된다고 생각
        idx += 1

    print(result)
```


###### 2. 곱하기 혹은 더하기 (312pg)
```python
if __name__ == '__main__':
    # 입력받은 문자열 숫자 하나씩 분리해서 리스트에 저장
    S = list(map(int, list(input())))

    # 리스트의 첫 값은 무조건 더하기 위해
    result = 0
    for num in S:
        # 피연산자 둘 다 0이 아니면 더하는 것보다 곱하는 것이
        # 무조건 더 커진다. 처음 result를 0으로 초기화 해줬으므로
        # 리스트의 첫 값은 더해준다.
        if result != 0 and num != 0:
            result += num
        else:
            result *= num

    print(result)
```

**오답정리**
```python
if __name__ == '__main__':
    S = list(map(int, input()))

    result = 0
    for num in S:
        # 1 일 때도 곱하는 것보다 더하는 것이 값이 더 커진다
        if result > 1 and num > 1:
            result *= num
        else:
            result += num

    print(result)
```


###### 4. 만들 수 없는 금액 \*
**오답정리**
화폐 단위를 기준으로 오름차순 정렬한다. 이후에 1부터 차례대로 특정한 금액을 만들 수 있는지 확인하면 된다. 1부터 target - 1까지의 모든 금액을 만들 수 있다고 가정해보자. 우리는 화폐 단위가 작은 순서대로 동전을 확인하며, 현재 확인하는 동전을 이용해 target 금액 또한 만들 수 있는지 확인하면 된다.
예를 들어 1, 2, 3 동전이 있을 때 1~6까지 만들 수 있으면, 1, 2, 3, 5 동전이 주어지면 6 + 5 = 11 까지 만들 수 있다. 이렇게 차례대로 동전을 확인하고 target 값을 업데이트 해준다.

[교재코드](.\python-for-coding-test-master\11\4.py)


###### 5. 볼링공 고르기
```python
if __name__ == '__main__':
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.sort()  # 공 무게별 오름차순 정렬

    result = 0
    idx = 0
    # 공 무게는 1부터 M까지 있는데, 맨 마지막에 M무게 공만
    # 남았을 때는 서로 다른 무게를 고를 수 없으므로 M 이전까지
    for weight in range(1, M):
        count = 0   # 현재 무게의 공 개수
        while weights[idx] == weight:
            idx += 1
            count += 1

        # 현재 무게의 공 개수와 이 보다 더 무거운 공 개수를 곱한다
        # 더 가벼운 무게의 공과의 계산은 이전에 행해졌다.
        result += (count * (len(weights) - idx))

    print(result)
```    

Counter를 이용
```python
if __name__ == '__main__':
    N, M = map(int, input().split())
    weights = collections.Counter(map(int, input().split()))

    result = 0
    for i in range(1, M):
        N -= weights[i]
        result += N * weights[i]

    print(result)
```