class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1)
        m = len(text2)

        return self.LCS(text1, text2, n , m)

    @cache
    def LCS(self, X, Y , n , m):

        if n == 0 or m == 0:
            return 0

        elif X[n-1] == Y[m-1]:
            return 1 + self.LCS(X, Y, n-1, m-1)

        elif X[n-1] != Y[m-1]:
            c1 = self.LCS(X, Y , n-1, m)
            c2 = self.LCS(X, Y, n, m-1)
            return max(c1, c2)