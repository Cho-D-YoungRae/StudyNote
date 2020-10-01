#### bisect
---
- 이진 탐색을 쉽게 구현할 수 있도록 하는 라이브러리
- '정렬된 배열'에서 효과적

###### bisect_left(), bisect_right()
> 대표적으로 위 두 메소드가 사용되며, 시간 복잡도는 O(logN)
- `bisect_left(a, x)`: 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메소드
- `bisect_right(a, x)`: 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메소드
> 1, 2, (bisect_left(a, 4)), 4, 4, (bisece_right(a, 4)), 8
```python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))
```
> 2 
>
> 4

###### 정렬된 리스트에서 특정 범위에 속하는 원소 개수
```python
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisec_left(a, left_value)
  return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))

print(count_by_range(a, -1, 3))
```
> 2
>
> 6