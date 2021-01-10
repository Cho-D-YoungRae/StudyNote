from typing import *


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0]
        result = []

        for interval_start, interval_end in intervals[1:]:
            if start <= interval_start <= end:
                if interval_end > end:
                    end = interval_end
            else:
                result.append([start, end])
                start, end = interval_start, interval_end

        result.append([start, end])

        return result