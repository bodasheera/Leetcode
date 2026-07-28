# Memoization

class Solution:



    def climbStairs(self, n: int) -> int:

        t = [-1] * (n+1) 

        def solve(n):
            
            # base case 
            if n <= 2:
                return n

            if t[n] != -1:
                return t[n]

            # hypothesis + induction
            t[n] =  solve(n-2) + solve(n-1)
            return t[n]

        return solve(n)