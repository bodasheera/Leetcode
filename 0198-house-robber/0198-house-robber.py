from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:


        n = len(nums)
        t = [-1] * (n+1)
        
        def solve(n):

            if n <= 0:
                return 0

            if n == 1:
                return nums[0]

            if t[n] != -1:
                return t[n]

            choice1 = nums[n-1] + solve(n-2) 
            choice2 = solve(n-1)

            t[n] = max(choice1 , choice2)
            return t[n]


        return solve(n)