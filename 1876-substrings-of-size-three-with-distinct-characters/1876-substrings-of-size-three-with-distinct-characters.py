class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        

        k = 3 
        i = 0
        j = 0

        calc = [0] * 26
        ans = 0

        while j < len(s):

            # calc
            index = ord(s[j]) - ord('a')
            calc[index] += 1

            # small window
            if j - i + 1 < k:
                j += 1

            # yo found the window
            elif j - i + 1 == k :

                # since all unique
                if max(calc) == 1:
                    ans += 1

                # fix the calc 
                index = ord(s[i]) - ord('a')
                calc[index] -= 1

                # slide the window 
                i += 1
                j += 1
        
        return ans