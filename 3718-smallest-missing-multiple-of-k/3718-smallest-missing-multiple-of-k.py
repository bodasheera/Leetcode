class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        

        num_set = set(nums)

        i = k
        while True:

            if i not in nums:
                return i

            i += k

        