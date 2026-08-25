class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        # Approach 1
        # num_set = set(nums)

        # i = k
        # while True:

        #     if i not in num_set:
        #         return i

        #     i += k

        
        # Approach 2

        target = k
        nums.sort() # nlogn

        for n in nums:

            if n == target:
                target += k

            elif n > target:
                return target

        return target

