class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        avg = float("-inf")
        total = 0

        l = 0
        r = 0

        while r < len(nums):

            total = total + nums[r]

            if r - l + 1 == k:
                avg = max(avg, total/k)
                total = total - nums[l]
                l = l + 1


            r = r + 1

        return avg