class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        
        sum1 = 0
        sum2 = 0

        for n in nums:

            if n < 10:
                sum1 += n

            else:
                sum2 += n

        return sum1 != sum2