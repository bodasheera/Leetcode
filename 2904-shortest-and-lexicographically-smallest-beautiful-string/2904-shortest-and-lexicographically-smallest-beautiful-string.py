class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        # variable sized sliding window

        i = 0
        j = 0
        res = ""
        freq = defaultdict(int)

        while j < len(s):

            freq[s[j]] += 1

            cond = freq['1']

            # smaller window
            # skipped as j + 1 in the end 

            # bigger window
            if cond > k:
                while cond > k:
                    freq[s[i]] = freq[s[i]] - 1
                    i = i + 1
                    cond = freq['1']

            # matching window
            if cond == k:

                # remove leading 0 if exists
                while s[i] == '0':
                    freq[s[i]] -= 1
                    i += 1
                
                curr = s[i : j + 1]

                if not res or len(curr) < len(res):
                    res = curr
                elif len(res) == len(curr) and curr < res:
                    res = curr

            # move the window 
            j = j + 1


        return res



