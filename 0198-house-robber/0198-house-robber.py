from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def solve(n):

            if n <= 0:
                return 0

            if n == 1:
                return nums[0]

            choice1 = nums[n-1] + solve(n-2) 
            choice2 = solve(n-1)

            return max(choice1 , choice2)

        n = len(nums)
        return solve(n)