#### [937_Reorder_Data_in_Log_Files](https://leetcode.com/problems/reorder-data-in-log-files/)


###### My Solution #1 - python -> wrong
```python
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

        letter_logs.sort(key=lambda x: x[1:])

        return list(map(" ".join, letter_logs))+digit_logs
```
> Input
["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

> Output
["g1 act car","a2 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

> Expected
["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

###### My Solution #2 - python
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []    # 문자 로그를 담는 리스트
        digit_logs = []     # 정수 로그를 담는 리스트

        for log in logs:
            to_list = log.split()   # 로그문자열을 공백으로 나눈 리스트로
            if to_list[1].isalpha():    # 문자 로그
                letter_logs.append(to_list)
            else:   # 숫자 로그
                digit_logs.append(" ".join(to_list))

        # 문자로그를 로그, 식별자 -> 사전순 으로 정렬
        letter_logs.sort(key=lambda x: (x[1:], x[0]))

        # 문자 로그 리스트 들을 다시 문자열로 바꾸고 정수 리스트와 결합
        return list(map(" ".join, letter_logs))+digit_logs
```        

> Runtime: 36 ms, faster than 77.86% of Python3 online submissions for Reorder Data in Log Files.


> Memory Usage: 13.9 MB, less than 50.12% of Python3 online submissions for Reorder Data in Log Files.
