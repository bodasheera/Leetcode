class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        sum = 0
        prod = 1

        while n :

            n, d= divmod(n, 10)
            sum  += d
            prod *= d

        return prod - sum
            


