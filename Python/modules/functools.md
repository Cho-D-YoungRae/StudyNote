#### functools

###### reduce

```python
import functools
import operator

a = [1, 2, 3, 4, 5]

functools.reduce(lambda x, y: x + y, a)
functools.reduce(lambda x, y: x + y, a, 0)  # 0은 초기값
functools.reduce(operator.add, a)
```

> ((((1+2)+3)+4)+5)