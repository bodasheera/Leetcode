# Memoization

class Solution:



    def climbStairs(self, n: int) -> int:

        t = [-1] * (n+1) 

        # def solve(n):
            
        #     # base case 
        #     if n <= 2:
        #         return n

        #     if t[n] != -1:
        #         return t[n]

        #     # hypothesis + induction
        #     t[n] =  solve(n-2) + solve(n-1)
        #     return t[n]

        # return solve(n)

        if n <= 2:
            return n
        
        t[0] = 0
        t[1] = 1
        t[2] = 2

        for i in range(3, n+1):

            t[i] = t[i-2] + t[i-1]

        return t[n]