class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        wt = coins
        W = amount 
        n = len(wt)

        t = [ [0] * (W+1) for _ in range(n+1) ]


        # initialize 1st row
        for j in range(W+1):
            t[0][j] = float('inf')

        # initialize 1st col
        for i in range(1, n+1):
            t[i][0] = 0

        # twist initialize 2nd row 
        for j in range(1, W+1):

            if j % coins[0] == 0:
                t[1][j] = j // coins[0]
            else:
                t[1][j] = float('inf')


        for i in range(2, n+1):
            for j in range(1, W+1):

                if wt[i-1] <= j:
                    c1 = 1 + t[i][j- wt[i-1]]
                    c2 = 0 + t[i-1][j]

                    t[i][j] = min(c1, c2)

                elif wt[i-1] > j:
                    t[i][j] = 0 + t[i-1][j]    

        return t[n][W] if t[n][W] != float('inf') else -1

    

