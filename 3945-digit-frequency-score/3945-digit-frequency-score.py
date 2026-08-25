from collections import Counter

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        
        freq = defaultdict(int)

        while n:
            n, d = divmod(n , 10)
            freq[d] += 1

        total = 0
        for d , count in freq.items():

            total += d * count

        return total

        