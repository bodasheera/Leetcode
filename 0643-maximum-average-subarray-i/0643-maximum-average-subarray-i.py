class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        

        l = 0
        max_total = float("-inf")
        total = 0

        for r in range(len(nums)):

            total = total + nums[r]

            if r - l + 1 == k:

                max_total = max(max_total , total)
                total = total - nums[l]
                l += 1

        return max_total/k