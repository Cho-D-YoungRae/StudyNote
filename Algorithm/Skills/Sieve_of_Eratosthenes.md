#### 에라토스테네스의 체
---
> N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있다.

1. 2부터 N까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i를 제외한 i의 배수를 모두 제거한다.
4. 더 이상 반복할 수 없을 때 까지 2번과 3번의 과정을 반복한다.

**python**
```python
import math

n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1): # n의 제곱근 까지만 확인하면 된다
  if array[i] == True: # i가 소수 or 남은 수
    j = 2
    while i * j <= n:
    array[i*j] = False
    j += 1
```
True로 남아있는 수는 소수.

메모리를 많이 차지한다는 단점이 있다.



[위키백과](https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4)
