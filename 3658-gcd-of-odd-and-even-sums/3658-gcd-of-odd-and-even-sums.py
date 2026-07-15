class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        
        i = 1
        odd_sum =0
        even_sum =0

        while i <= 2*n:
            odd_sum = odd_sum + i
            i = i + 2

        i = 2
        while i <= 2*n:
            even_sum = even_sum + i
            i = i + 2

        n1 = odd_sum
        n2 = even_sum

        rem = 0

        while n1 > 0:

            d = n2 // n1 
            r = n2 % n1 

            n2 = n1 
            n1 = r 

        return n2

