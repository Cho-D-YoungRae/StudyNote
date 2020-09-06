
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.upper())
        result = []
        for ch in s:
            if ch.isalnum():
                result.append(ch)


        return result == result[::-1]



if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome("race a car"))

