class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        

        i = 1

        total = nums[0]

        while i < len(nums):

            if nums[i] == nums[i-1] + 1:
                total = total + nums[i]

            else:
                break

            i += 1

        while True:

            if total not in nums:
                return total
            
            else:
                total = total + 1


        
        
        
            



