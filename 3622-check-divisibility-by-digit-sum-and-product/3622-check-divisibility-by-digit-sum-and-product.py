class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        total = 0
        prod = 1

        original_n = n

        while n:

            n , d = divmod(n , 10)
            total += d
            prod *= d


        return (original_n % (total + prod)) == 0