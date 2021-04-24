#### defaultdict 순회

```python
graph = collections.defaultdict(list)
...
# 오류 발생
for x in graph:
    ...

# 아래 방법으로
for x in list(graph):
    ...
```

defaultdict을 순회할 때 첫번째 방법으로 순회를 진행하면 `RuntimeError: dictionary changed size during iteration` 오류가 발생한다. defaultdict은 키가 없는 딕셔너리에 대해서 빈 값 조회시 NULL오류가 발생하지 않도록 처리가 되어있다. 이 때문에 존재하지 않는 키를 조회할때 오류를 내지 않게 하기 위해 디폴트를 생성하게 되고 그러면서 오류가 발생한다.

두번째 방법으로 진행하면 새로운 리스트를 생성하는 것이므로 오류가 발생하지 않는다.