#### [49_Group_Anagrams](https://leetcode.com/problems/group-anagrams/)

###### My Solution 1
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        group_dict = collections.defaultdict(list)

        # 애너그램을 만족한다면 단어 내에 알파벳 개수는 어처피 동일
        # 정렬해서 같은 단어가 나오면 애너그램이다
        for word in strs:
            group_dict[''.join(sorted(word))].append(word)

        result = []
        for k in group_dict:
            result.append(group_dict[k])

        return result
```
> Runtime: 104 ms, faster than 72.75% of Python3 online submissions for Group Anagrams.

> Memory Usage: 16.6 MB, less than 84.81% of Python3 online submissions for Group Anagrams.           

###### My Solution 1-1
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        group_dict = collections.defaultdict(list)
        for word in strs:
            group_dict[''.join(sorted(word))].append(word)

        return list(group_dict.values())
```

>Runtime: 96 ms, faster than 93.42% of Python3 online 
submissions for Group Anagrams.

>Memory Usage: 16.9 MB, less than 71.13% of Python3 online submissions for Group Anagrams.

동일한 풀이법. 내부함수를 이용하여 더 깔끔해지고 조금의 성능 개선이 있다.