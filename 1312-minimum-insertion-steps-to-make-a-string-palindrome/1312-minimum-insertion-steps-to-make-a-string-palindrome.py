class Solution:
    def minInsertions(self, s: str) -> int:

        r = s[::-1]

        n = len(s)
        m = n

        t = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):

                if s[i-1] == r[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]

                elif s[i-1] != r[j-1]:
                    c1 = t[i-1][j]
                    c2 = t[i][j-1]

                    t[i][j] = max(c1, c2)

        # its actually lps 
        lps = t[n][m]

        # this is actually min deletions 
        # but its same as min insertions
        return n - lps


