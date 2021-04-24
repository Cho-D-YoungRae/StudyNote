# [239_Sliding_Window_Maximum](https://leetcode.com/problems/sliding-window-maximum/)

## Try1 - 시간초과
```python
from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i:i+k]))

        return result
```

해당되는 범위의 슬라이드마다 최댓값을 계산한다.

## Try2 - 시간초과
```python
from typing import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        maxinslide = None	# 슬라이드 내 최댓값
        for i in range(len(nums) - k + 1):
            if not maxinslide:	# 최댓값 지정되어 있지 않으면
                maxinslide = max(nums[i:i+k])	# 최댓값 지정
            else:	# 지정되어 있으면
                maxinslide = max(maxinslide, nums[i+k-1]) # 새로들어온 값과 비교

            result.append(maxinslide)	# 최댓값을 답에 추가
            if maxinslide == nums[i]:	# 최댓값이 슬라이드에서 빠지면
                maxinslide = None	# 최댓값을 None으로

        return result
```

## Try 3
```python
from typing import *
import heapq
from collections import Counter

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        slide_counter = Counter() # 슬라이드 내 숫자 개수

		# 슬라이드 보다 1개 작게 힙과 카운터에 넣는다.
        for i in range(k - 1):
            heapq.heappush(heap, -nums[i])
            slide_counter[nums[i]] += 1
		
        # 슬라이드 마지막 인덱스를 기준으로 반복문
        for i in range(k-1, len(nums)):
        	# 힙과 카운터에 값 넣는다
            heapq.heappush(heap, -nums[i])
            slide_counter[nums[i]] += 1
			
            # 힙에서 최댓값을 꺼낸다.
            maxinslide = -heapq.heappop(heap)
            # 최댓값이 슬라이드에 없으면
            # 슬라이드에 있는 숫자가 나올 때까지 꺼낸다.
            while slide_counter[maxinslide] == 0:
                maxinslide = -heapq.heappop(heap)
			
            result.append(maxinslide)	# 결과에 추가
            heapq.heappush(heap, -maxinslide)	# 힙에 다시 넣는다 -> 다음 꺼낼 때를 위해
            slide_counter[nums[i-k+1]] -= 1	# 슬라이드의 첫 값 카운터에서 줄인다.

        return result
```

## Try 4
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        result = []
        hp = []
        for i in range(k):
            heapq.heappush(hp, (-nums[i], -i))

        max_idx = -heapq.heappop(hp)[1]
        result.append(nums[max_idx])

        for i in range(1, len(nums)-k+1):
            while max_idx < i:
                max_idx =  -heapq.heappop(hp)[1]
            right_idx = i + k -1
            if nums[right_idx] > nums[max_idx]:
                max_idx = right_idx
            else:
                heapq.heappush(hp, (-nums[right_idx], -right_idx))

            result.append(nums[max_idx])
            
        return result
```
3번풀이와 유사하다. Counter를 사용하는 대신 인덱스를 이용해 슬라이드 내에 포함되는지 체크한다. 3번은 반복문이 한번 돌 때마다 heap에 push, pop하는데 이 풀이는 필요시만 한다.

## 참고풀이 1 - 시간초과
> `파이썬 알고리즘 인터뷰` - 571pg
```python
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
       	
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:	# k번은 그냥 슬라이드에 추가
                continue

            # 새로 추가된 값이 기존 최대값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(current_max)

            # 최대값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')
        return results
```        
교재에 있던 풀이 인데 입력 예시가 추가되었는지 이제 시간초과가 뜬다.
Try2 와 풀이가 유사

