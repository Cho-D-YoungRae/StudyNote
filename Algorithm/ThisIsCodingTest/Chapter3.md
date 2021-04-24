#### Chapter 03. 그리디

###### 큰 수의 법칙 (92pg)
```python
N, M, K = map(int, input().split())
    
numList = list(map(int, input().split()))

numList.sort(reverse=True)

d, m = divmod(M, K+1)

result = numList[0]*(d*K + m) + numList[1]*d

print(result)
```

###### 숫자 카드 게임 (96pg)
```python
def main():
  N, M = map(int, input().split())

  cards = []
  result = -float("inf")
  for i in range(N):
    cards.append(list(map(int, input().split())))
    result = max(result, min(cards[i]))

  print(result)

  
main()
```

###### 1이 될 때까지 \*
```python
def main():
  N, K = map(int, input().split())

  result = 0
  while N != 1:
    if N % K == 0:
      N //= K
    else:
      N -= 1
    
    result += 1

  print(result)
  
main()
```

오답 정리
```python
def main():
  N, K = map(int, input().split())

  result = 0
  # N이 K와 제곱관계가 아니면 1로 꼭 나누어지지 않을 수 있으므로
  while N >= K:
    if N % K == 0:
      N //= K
    else:
      N -= 1
    result += 1

  while N > 1:
    result += 1
    N -= 1

  print(result)
  
main()
```