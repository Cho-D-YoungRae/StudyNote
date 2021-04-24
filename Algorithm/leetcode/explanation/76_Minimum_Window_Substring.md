# [76_Minimum_Window_Substring](https://leetcode.com/problems/minimum-window-substring/)



## 참고 풀이
> `파이썬 알고리즘 인터뷰` - 575pg
```python
from typing import *
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t) # 필요한 문자 조건
        # missing이 없으면 Counter의 키를 순회하며 하나하나 조건만족 확인해야한다
        missing = len(t) # 필요한 문자 총 개수
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            # need[char] 이 양수일 때만 missing을 감소시킨다.
            # t에 없었던 문자라면 항상 0이하일 것이다.
            # t에 있었던 문자 중 필요한 개수가 있다면 0이하일 것이다 
            # -> missing 감소 안함
            missing -= need[char] > 0
            need[char] -= 1

            if missing == 0: # 모든 t 조건 만족하면 왼쪽포인터 이동 -> 슬라이드 크기 줄이기
                # t의 문자 개수가 슬라이드 내에 딱 맞게 있으면 need[s[left]] == 1
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1 # t에 없던 문자는 최대 0까지만 증가할 것이다.
                    left += 1
                
                # 슬라이더 크기 갱신
                if not end or right - left <= end - start:
                    start, end = left, right
                    
                # 슬라이드의 양쪽 끝에는 t조건에 맞는 문자가 있을 것이다 
                # -> 그래야 슬라이드가 작아질 수 있으므로
                # 조건을 만족하는지 확인 후 크기 갱신도 했으므로
                # 다음 슬라이드를 찾기위해 왼쪽 포인터 증가
                # -> 조건에 맞는 문자 하나 감소한다.
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]
```





