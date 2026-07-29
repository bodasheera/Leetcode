

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)

        t = [-1] * (n+1)

        # def solve(n):

        #     # base case
        #     # when we start no cost 
        #     # we can start at 0 and 1

        #     if n <= 1:
        #         return 0

        #     if t[n] != -1:
        #         return t[n]

        #     # hypothesis
        #     # we can end at n or n-1
        #     # pay the cost and solve for smaller input 

        #     # use n and solve smaller input
        #     c1 = cost[n-1] + solve(n-1) 

        #     # use n-1 and solve smaller input
        #     c2 = cost[n-2] + solve(n-2)

        #     # induction
        #     t[n] = min(c1, c2)

        #     return t[n]
 

        # return solve(n)

        # base case
        t[0] = 0
        t[1] = 0

        for i in range(2, n+1):

            c1 = cost[i-1] + t[i-1]
            c2 = cost[i-2] + t[i-2]

            t[i] = min(c1, c2)

        return t[n]