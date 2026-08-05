class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        

        def solve(n):

            if n <= 0:
                return False

            if n == 1:
                return True


            if abs(n) % 4 == 0:
                return solve( n // 4)
            else:

                return False

        return solve(n)

        