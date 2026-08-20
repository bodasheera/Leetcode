class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        n = len(s)

        ct = 0

        for i in range(1, n):

            if s[i-1].lower() != s[i].lower():
                ct += 1

        return ct
