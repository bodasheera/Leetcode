from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def solve(n):

            # base case
            if n <= 0:
                return 0

            if n == 1:
                return 0

            # hypothesis

            # use n and solve smaller input
            c1 = cost[n-1] + solve(n-1) 

            # use n-1 and solve smaller input
            c2 = cost[n-2] + solve(n-2)

            # induction
            return min(c1, c2)



        

        n = len(cost)

        return solve(n)