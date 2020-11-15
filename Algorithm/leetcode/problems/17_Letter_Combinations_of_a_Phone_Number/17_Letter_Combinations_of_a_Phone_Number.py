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