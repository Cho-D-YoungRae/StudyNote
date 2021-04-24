#### [23_Merge_k_Sorted_Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
> 274pg


###### My Solution 1 -> WRONG
```python
from typing import *
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for i in range(len(lists)):
            while lists[i]:
                ## 에러가 발생한 부분
                heapq.heappush(heap, (lists[i].val, lists[i]))
                ##
                lists[i] = lists[i].next

        result = pnode = ListNode()

        while heap:
            pnode.next = heapq.heappop(heap).pop()
            pnode = pnode.next

        pnode.next = None

        return result.next
```

`TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'` 라는 에러가 발생한다. `중복된 값을 넣을 수 없다` 라는 뜻이다.

ListNode.val 의 값은 중복이 될 수 있다. 그 다음 비교 대상인 ListNode 는 비교 연산이 불가능하기 때문에 위 오류가 발생한다.

나는 리스트의 노드를 하나 하나 씩 다 따로 저장했다. 그러다보니 중복에 대한 처리가 더 어렵다. 리스트 단위로 저장해 그 리스트에서 노드 하나 씩 꺼내서 사용하는 식으로 해결할 수 있다.

###### My Solution 1-1