class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        

        def solve(arr , index):

            # base condition
            if len(arr) == 1:
                return arr[0]

            # hypothesis

            index = (index + k) % len(arr)
            del arr[index]

            return solve(arr, index)


        

        k = k - 1
        arr = []
        for i in range(0, n):
            arr.append(i + 1)
        return solve(arr, 0)