class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # nums.sort()

        # return ( nums[-1] -1 ) * (nums[-2]  -1 )

        biggest = -1
        second_biggest = -1

        for n in nums:

            if n > biggest:
                second_biggest = biggest
                biggest = n

            elif n > second_biggest:
                second_biggest = n

        return ( biggest -1 ) * (second_biggest  -1 )