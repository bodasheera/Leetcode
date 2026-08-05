from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i = 0
        j = 0
        n = len(s)

        mx = 0

        uniq = set()

        while j < n:

            # condition 
            while s[j] in uniq:
                uniq.remove(s[i])
                i += 1

            uniq.add(s[j]) # now pakka unique

            mx = max(mx , j - i + 1)
            j += 1

        return mx
