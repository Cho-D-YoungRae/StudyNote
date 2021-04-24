#### 런너 기법

런너(Runner)는 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법이다. 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다. 2개의 빠른 런너(Fast Runner) 느린 런너(Slow Runner)라고 부르는데, 대개 빠른 런너(포인터)는 두 칸씩 건너뛰고 느린 런너(포인터)는 한 칸씩 이동하게 한다. 이때 빠른 런너가 연결 리스트의 끝에 도달하면, 느린 런너는 정확히 연결리스트의 중간 지점을 가리키게 된다. 이같은 방식으로 중간 위치를 찾아내면, 여기서부터 값을 비교하거나 뒤집기를 시도하는 등 여러모로 활용할 수 있다.

```python
rev = None  # 중간 앞 부분을 반대로 연결시킨다.
slow = fast = head  # head 는 연결 리스트의 head

while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next

if fast:
    slow = slow.next
```