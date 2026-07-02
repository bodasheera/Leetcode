class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        

        n = len(stones)
        Range = W = sum(stones)
        wt = stones 

        # we need only s1 . we can calculate s2 using range
        all_s1 = self.subsetSum(wt, W//2, n)

        res = float('inf')
        for i in range(len(all_s1)):
            if all_s1[i]:
                res = min(res, Range - 2* i )

        return res




    
    def subsetSum(self, wt, W, n):

        t = [[False] * (W+1) for i in range(n+1)]

        for i in range(n+1):
            t[i][0] = True

        for i in range(1, n+1):
            for j in range(1, W+1):

                if wt[i-1] <= j:
                    c1 = t[i-1][j - wt[i-1]]
                    c2 = t[i-1][j]
                    t[i][j] = c1 or c2

                elif wt[i-1] > j:
                    t[i][j] = t[i-1][j]
        
        # last row has sum possibilities for all numbers
        return t[n]



