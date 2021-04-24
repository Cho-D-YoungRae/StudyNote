#### [344_Reverse_String](https://leetcode.com/problems/reverse-string/)


###### My Solution - python
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        front, back = 0, len(s) - 1

        while front < len(s)//2:
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1
```
>Runtime: 220 ms, faster than 54.44% of Python3 online submissions for Reverse String.

> Memory Usage: 18.3 MB, less than 61.83% of Python3 online submissions for Reverse String.


###### list.reverse()
리스트에 제공되는 함수이다.