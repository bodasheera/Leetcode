class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # LCS
        n = len(word1)
        m = len(word2)

        t = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                
                
                if word1[i-1] == word2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                    
                elif word1[i-1] != word2[j-1]:
                    
                    c1 = t[i][j-1]
                    c2 = t[i-1][j]
                    t[i][j] = max(c1, c2)
                    
        lcs = t[n][m]
        deletion = n - lcs
        insertion = m - lcs

        return insertion + deletion
        	    