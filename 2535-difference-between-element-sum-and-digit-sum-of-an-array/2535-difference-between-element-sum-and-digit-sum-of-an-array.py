class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        ele_sum = sum(nums)

        digit_sum = 0

        for n in nums:

            while n:
                n , d = divmod(n, 10)
                digit_sum += d

        return abs(ele_sum - digit_sum)
