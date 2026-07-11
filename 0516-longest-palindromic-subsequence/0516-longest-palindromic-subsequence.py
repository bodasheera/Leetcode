class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        

        s1 = s
        s2 = s[::-1]

        n = len(s1)
        m = len(s2)

        # LCS    
        t = [[0] * (m+1) for _ in range(n+1) ]


        for i in range(1, n+1):
            for j in range(1, m+1):

                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]

                elif s1[i-1]  != s2[j-1]:
                    c1 = t[i][j-1]
                    c2 = t[i-1][j]
                    t[i][j] = max(c1, c2)

        return t[n][m]

