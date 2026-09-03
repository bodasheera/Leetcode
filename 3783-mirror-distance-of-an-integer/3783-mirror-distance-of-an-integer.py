class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        num = n
        if n < 10:
            rev = n
        else:

            rev = 0
            while n > 0:
                n,d = divmod(n, 10)
                rev = rev * 10 + d

        return abs(num - rev)