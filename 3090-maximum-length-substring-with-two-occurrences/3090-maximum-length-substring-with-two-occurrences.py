class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        i = 0
        j = 0
        count = {}

        k = 2
        res = 0

        while j < len(s):

            count[s[j]] = count.get(s[j], 0) + 1

            #cond = max(count.values()) 
            cond = count[s[j]]

            if cond <= k:
                res = max(res, j - i + 1)
                j += 1

            if cond > k:
                while cond > k:
                    count[s[i]] -= 1
                    if count[s[i]] == 0:
                        del count[s[i]]
                    #cond = max(count.values())
                    cond = count[s[j]]
                    i += 1

                j += 1

        return res