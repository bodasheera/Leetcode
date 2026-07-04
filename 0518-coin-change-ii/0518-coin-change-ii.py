class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        W = amount
        wt = coins
        n = len(wt)

        return self.subsetSum(wt, W, n)
        


    def subsetSum(self, wt , W , n):

        t = [[0] * (W+1) for _ in range(n+1)]

        for i in range(n+1):

            t[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, W+1):

                if wt[i-1] <= j:
                    c1 = t[i][j - wt[i-1]]
                    c2 = t[i-1][j]
                    t[i][j] = c1 + c2

                elif wt[i-1] > j:
                    t[i][j] = t[i-1][j]

        return t[n][W]