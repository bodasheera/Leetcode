class Solution:
    def triangleType(self, nums: List[int]) -> str:

        total = sum(nums)

        for n in nums:
            if total - n <= n:
                return "none"
        

        uniq = set()

        for n in nums:
            uniq.add(n)

        if len(uniq) == 1:
            return "equilateral"

        elif len(uniq) == 2:
            return "isosceles"

        elif len(uniq) == 3:
            return "scalene"
        
        