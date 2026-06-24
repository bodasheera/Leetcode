class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        counter = [0] * (len(nums) + 1)
        res = []

        for n in nums:
            counter[n] = 1

        i = 1

        while i < len(nums) + 1:

            if counter[i] == 0:
                res.append(i)

            i += 1

            

        return res