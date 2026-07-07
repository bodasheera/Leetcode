class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        n = len(text1)
        m = len(text2)
        t = [[-1] * (m+1) for _ in range(n+1)]

        return self.LCS(text1, text2, n , m, t)


    def LCS(self, X, Y , n , m, t):

        # base case
        if n == 0 or m == 0:
            return 0

        if t[n][m] != -1:
            return t[n][m]

        elif X[n-1] == Y[m-1]:
            t[n][m] =  1 + self.LCS(X, Y, n-1, m-1, t)
            return t[n][m]

        elif X[n-1] != Y[m-1]:
            c1 = self.LCS(X, Y , n-1, m, t)
            c2 = self.LCS(X, Y, n, m-1, t)
            t[n][m] = max(c1, c2)
            return t[n][m]