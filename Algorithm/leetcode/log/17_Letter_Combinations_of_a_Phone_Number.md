#### [17_Letter_Combinations_of_a_Phone_Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
> 338 pg


###### My Solution 1
```python
from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letter = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}

        def dfs(digits):
            if len(digits) == 1:
                return list(digit_to_letter[digits])
            else:
                result = []
                for first_letter in digit_to_letter[digits[0]]:
                    for letters in dfs(digits[1:]):
                        result.append(first_letter + letters)

                return result

        return dfs(digits)
```

> Runtime: 28 ms, faster than 79.50% of Python3 online submissions for Letter Combinations of a Phone Number.

> Memory Usage: 13.9 MB, less than 83.16% of Python3 online submissions for Letter Combinations of a Phone Number.
