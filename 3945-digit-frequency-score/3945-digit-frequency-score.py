from collections import Counter

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        
        total = 0

        while n:
            n, d = divmod(n , 10)
            total += d

        return total

        