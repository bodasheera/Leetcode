class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        s = s.lower()

        n = len(s)

        ct = 0

        for i in range(1, n):

            if s[i-1]!= s[i]:
                ct += 1

        return ct
