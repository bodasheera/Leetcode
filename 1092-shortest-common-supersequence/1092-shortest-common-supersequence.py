class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        

        # lcs 
        n = len(str1)
        m = len(str2)

        t = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):

                if str1[i-1] == str2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]

                elif str1[i-1] != str2[j-1]:
                    c1 = t[i-1][j]
                    c2 = t[i][j-1]

                    t[i][j] = max(c1, c2)

        # lcs matrix is ready now 

        # backtrack and get the SCS

        i = n
        j = m 
        res = []

        while i > 0 and j > 0:

            if str1[i-1] == str2[j-1]:
                res += str1[i-1]
                i = i -1
                j = j -1

            elif str1[i-1] != str2[j-1]:

                if t[i-1][j] >= t[i][j-1]:
                    res.append(str1[i-1])
                    i = i - 1

                elif t[i][j-1] > t[i-1][j]:
                    res.append(str2[j-1])
                    j = j - 1

        
        # if i > 0 means string1 still exists 
        # lcs was zero "ab" and ""
        # scs of "ab" and "" is "ab"

        while i > 0:
            res.append(str1[i-1])
            i -= 1

        while j > 0:
            res.append(str2[j-1])
            j -= 1

        return "".join(res[::-1])
