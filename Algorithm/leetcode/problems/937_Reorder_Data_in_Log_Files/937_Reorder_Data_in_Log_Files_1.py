from typing import *


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            to_list = log.split()
            if to_list[1].isalpha():
                letter_logs.append(to_list)
            else:
                digit_logs.append(" ".join(to_list))

        letter_logs.sort(key=lambda x: (x[1:], x[0]))

        return list(map(" ".join, letter_logs))+digit_logs

