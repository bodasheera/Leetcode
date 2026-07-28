from functools import cache

class Solution:

    @cache
    def climbStairs(self, n: int) -> int:
        
        # base case 
        if n <= 2:
            return n

        # hypothesis + induction
        return self.climbStairs(n-2) + self.climbStairs(n-1)