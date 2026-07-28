from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:


        n = len(nums)
        t = [-1] * (n+1)

        t[0] = 0
        t[1] = nums[0]
        
        # def solve(n):

        #     if n <= 0:
        #         return 0

        #     if n == 1:
        #         return nums[0]

        #     if t[n] != -1:
        #         return t[n]

        #     choice1 = nums[n-1] + solve(n-2) 
        #     choice2 = solve(n-1)

        #     t[n] = max(choice1 , choice2)
        #     return t[n]


        # return solve(n)

        for i in range(2, n+1):

            c1 = nums[i-1] + t[i-2]
            c2 = t[i-1]

            t[i] = max(c1, c2)

        return t[n]