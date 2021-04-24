#### [819_Most_Common_Word](https://leetcode.com/problems/most-common-word/)

**My Solution 1**
python
```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-zA-Z]', ' ', paragraph)
        paragraph = paragraph.lower()
        word_count = collections.Counter(paragraph.split())

        for word, i in word_count.most_common():
            if word not in banned:
                return word
```
>Runtime: 76 ms, faster than 5.22% of Python3 online submissions for Most Common Word.

>Memory Usage: 14 MB, less than 28.55% of Python3 online submissions for Most Common Word.                


**1번 반성**
```python
words = [word for word in re.sub('[^\w]', ' ', paragraph)\
            .lower().split() if word not in banned]
```   
리스트 컴프리헨션으로 구성하면 더 깔끔하고 빠르게 된다.     