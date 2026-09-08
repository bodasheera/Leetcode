class Solution:
    def countCommas(self, n: int) -> int:
        
        # < 1000 0 commas
        # 1,000 - 100,000 - 1 comma

        if n < 1000:
            return 0

        total = n - 1000 + 1

        return total
        