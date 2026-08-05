class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        

        def solve(n):

            if n <= 0:
                return False

            if n == 1:
                return True


            if abs(n) % 3 == 0:
                return solve( n // 3)
            else:

                return False

        return solve(n)

        