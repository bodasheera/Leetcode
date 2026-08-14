class Solution:
    def countDigits(self, num: int) -> int:
        
        temp = num
        ct = 0

        while num:

            num , d = divmod(num, 10)

            if temp % d == 0:
                ct += 1

        return ct