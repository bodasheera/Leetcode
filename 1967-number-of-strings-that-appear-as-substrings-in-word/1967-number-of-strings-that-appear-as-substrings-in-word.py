class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        

        ct = 0

        for pattern in patterns:

            if pattern in word:
                ct += 1

        return ct