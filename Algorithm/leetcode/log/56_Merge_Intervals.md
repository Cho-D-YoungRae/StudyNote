#### [56_Merge_Intervals](https://leetcode.com/problems/merge-intervals/)

###### My Solution 1
```python
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0]
        result = []

        for interval_start, interval_end in intervals[1:]:
            if start <= interval_start <= end:
                # end = max(end, interval_end) # 개선된 방식
                if interval_end > end:
                    end = interval_end
            else:
                result.append([start, end])
                start, end = interval_start, interval_end

        result.append([start, end])

        return result
```

주석으로 표시한 부분으로 개선하자 실행 시간이 빨라졌다. 내부 함수를 이용하자.

**코드변경이전**
> Runtime: 148 ms, faster than 5.04% of Python3 online submissions for Merge Intervals.

> Memory Usage: 16.2 MB, less than 38.32% of Python3 online submissions for Merge Intervals.     

**개선된 후**
> Runtime: 84 ms, faster than 72.63% of Python3 online submissions for Merge Intervals.

> Memory Usage: 16.1 MB, less than 38.32% of Python3 online submissions for Merge Intervals.


