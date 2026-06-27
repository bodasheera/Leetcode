class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        

        l = 0
        avg = float("-inf")
        total = 0

        for r in range(len(nums)):

            total = total + nums[r]

            if r - l + 1 == k:

                avg = max(avg , total/k)
                total = total - nums[l]
                l += 1

        return avg