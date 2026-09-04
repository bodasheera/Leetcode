class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        prefix = []

        big = float('-inf')
        
        for n in nums:
            big = max(big, n)
            prefix.append(big)

        suffix = [0] * len(nums)

        small = float('inf')

        for i in range(len(nums) -1 , -1 , -1):
            small = min(small, nums[i])
            suffix[i] = small

        res = float('inf')
        for i in range(len(nums)):
            score = prefix[i] - suffix[i]

            if score <= k:
                res = min(res, i)

        return -1 if res == float('inf') else res


            






