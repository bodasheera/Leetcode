class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        n = len(s)
        m = len(t)

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):

                if s[i-1] == t[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                elif s[i-1] != t[j-1]:
                    c1 = dp[i-1][j]
                    c2 = dp[i][j-1]

                    dp[i][j] = max(c1, c2)

        lcs = dp[n][m]

        return n - lcs == 0