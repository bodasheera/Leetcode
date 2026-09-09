class Solution:
    def countCommas(self, n: int) -> int:
        

        # 1,000 - 999,999 - 1 - comma , 4- 6
        # 1,000,000 - 999,999,999 - 2 comma , 7 - 9
        # 1,000,000,000 - 999,999,999,999 - 3 comma , 10-12 
        # 1,000,000,000,000 - 9,999,999,999 - 4 comma 13- 15
        # 1,000,000,000,000,000 - 5 comma , 15 - 
        

        if n < 1000:
            return 0

        digits = len(str(n))

        start = 4
        end = 6
        commas = 1
        total = 0
        

        while True:
            if digits > end:
                num1 = 10 ** (start-1)
                num2 = (10 ** (end)) - 1

                total += (num2 - num1 + 1) * commas
            

            elif digits >= start and digits <= end:
                num1 = 10 ** (start-1)
                num2 = n
                total += (num2 - num1 + 1) * commas
                break

            start += 3
            end += 3
            commas += 1

        return total

