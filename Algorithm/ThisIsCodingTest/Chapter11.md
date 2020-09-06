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


###### 4. 만들 수 없는 금액
