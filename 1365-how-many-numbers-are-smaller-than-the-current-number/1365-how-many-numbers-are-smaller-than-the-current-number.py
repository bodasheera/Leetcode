class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        

        sorted_nums = sorted(nums)
        # 1,2,2,3,8

        pos = {}

        i = 0

        while i < len(sorted_nums):
            if pos.get(sorted_nums[i] , -1) == - 1:
                pos[sorted_nums[i]] =  i
            i += 1

        res = []

        for n in nums:
            res.append(pos[n])

        return res

        

            