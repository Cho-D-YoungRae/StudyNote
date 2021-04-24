#### 객체 복사

```python
a = [1, 2, 3]
b = a
c = a[:]
```
> id(a) == id(b) != id(c)

> 참조로 처리된 변수 b는 a와 동일한 ID를 갖지만 변수 c는 값 자체가 복사되어 새로운 객체가 되었다.

```python
d = a.copy
```

> 위와 같은 방법으로도 가능하다.

```python
import copy

a = [1, 2, [3, 6], 4]
b = copy.deepcopy(a)
```
> 깊은 복사