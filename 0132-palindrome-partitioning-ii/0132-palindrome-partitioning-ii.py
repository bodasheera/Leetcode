class Solution:
    
    def minCut(self, s: str) -> int:

        n = len(s)
        t = [-1] * (n+1)


        # simple palindrome memoization

        dp = [[False] * (n+1) for _ in range(n+1)]
        
        for i in range(n - 1, -1 , -1):
            for j in range(i , n):

                # one ele 
                # a , aa, aba all are palidromes 
                if s[i] == s[j] and j-i <= 2:
                    dp[i][j] = True

                # hypothesis and induction
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True

        def solve(i):

            # base case
            if i >= n:
                return 0

            if t[i] != -1:
                return t[i]

            # base case
            # palindrome table
            if dp[i][n-1]:
                t[i] = 0
                return 0

            mn = float('inf')

            for k in range(i, n):
                
                # hypothesis + induction


                if dp[i][k]:
                    temp = 1 + 0 + solve(k+1)

                    if temp < mn:
                        mn = temp

            t[i] = mn
            return t[i]



            

        return solve(0)

        
