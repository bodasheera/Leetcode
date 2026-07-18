class Solution:
    def findGCD(self, nums: List[int]) -> int:
        

        a = min(nums)
        b = max(nums)

        # while a != 0:

        #     r = b % a 

        #     b = a
        #     a = r

        # return b

        def gcd(x, y):

            # base case
            if y == 0:
                return x

            #hypothesis + induction
            return gcd( y , x % y)

        return gcd(b , a)
