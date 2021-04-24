#### itertools
---
###### permutations 클래스
---
iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우 (순열)
```python
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutation(data, 3)) # r = 3

print(result)
```
> [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

###### combinations 클래스
---
iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우 (조합)
```python
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))  # r = 2

print(result)
```
> [('A', 'B'), ('A', 'C'), ('B', 'C')]

###### product 클래스
iterable 객체에서 repeat개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열). 중복을 허용한다.
```python
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))  # repeat = 2

print(result)
```
> [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

###### combinations_with_replacement 클래스
iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합). 중복을 허용한다.
```python
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))  # r = 2

print(result)
```
> [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]