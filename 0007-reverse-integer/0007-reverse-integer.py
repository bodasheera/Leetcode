class Solution:
    def reverse(self, x: int) -> int:
        
        num = 0
        place = 0

        sign = 1

        if x < 0:
            sign = -1

        x = abs(x)

        size = 0
        temp = x
        while temp:
            temp,d = divmod(temp, 10)
            size += 1

        place = size -1 

        while x:
            x,d = divmod(x, 10)
            num = num + d * 10 ** place
            place -= 1

        if num < (-2**31) or num > (2**31) - 1:
            return 0
            
        return num * sign
