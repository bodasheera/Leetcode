class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        # infinite loop
        while True:

            number = n

            prod = 1

            while number:

                r = number % 10
                number = number // 10
                prod = prod * r

            print(prod)

            if prod % t == 0:
                return n

            n = n + 1


        