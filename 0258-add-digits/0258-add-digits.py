class Solution:
    def addDigits(self, num: int) -> int:
        
        total = 0

        while True:

            total = 0
            while num:

                d = num % 10
                total += d
                num = num // 10

            if total < 10:
                break


            num = total

            
        return total

            