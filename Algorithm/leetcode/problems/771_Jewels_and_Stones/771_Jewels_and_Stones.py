class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        SCounter = Counter(S)

        result = 0
        for jewel in J:
            result += SCounter[jewel]

        return result