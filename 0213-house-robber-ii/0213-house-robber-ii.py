from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        # Edge case: single house
        if n == 1:
            return nums[0]


        t1 = [-1] *(n+1)
        t2 = [-1] *(n+1)

        def solve(n, arr, t):

            if n <= 0:
                return 0

            if n == 1:
                return arr[0]

            if t[n] != -1:
                return t[n]

            # rob n house and smaller input 
            c1 = arr[n-1] + solve(n-2, arr, t) 

            # dont rob current house
            c2 = solve(n-1, arr, t)


            t[n] =  max(c1, c2)
            return t[n]

        # if we rob first house we can rob last house
        c1 = solve(n-1, nums[:-1] , t1)

        # if we rob last house we cant rob first house
        c2 = solve(n-1, nums[1:], t2)

        return max(c1, c2)



