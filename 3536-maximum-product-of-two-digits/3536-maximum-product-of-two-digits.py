class Solution:
    def maxProduct(self, n: int) -> int:
        
        digits = []
        prod = -1
        while n > 0:

            d = n % 10
            digits.append(d)
            n = n // 10



        max1 = -1
        max2 = -1

        for d in digits:

            if d > max1:
                max2 = max1
                max1 = d
            elif d > max2:
                max2 = d


        return max1 * max2

