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

        num_set = set(nums)


        while total in num_set:
            total += 1

        return total



        
        
        
            



