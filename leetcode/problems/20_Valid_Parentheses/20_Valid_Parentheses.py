class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(':')', '{':'}', '[':']'}
        stack = []
        for p in s:
            if p in pair:
                stack.append(pair[p])
            else:
                if stack and stack[-1] == p:
                    stack.pop()
                else:
                    return False
                
        return len(stack) == 0