from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:


        count = Counter(s)

        pos = float('inf')

        for k, v in count.items():

            if v == 1:
                
                for i in range(len(s)):

                    if s[i] == k:
                        pos = min(pos , i)
                        break 

        return -1 if pos == float('inf') else pos



        # TLE
        # for i in range(len(s)):

        #     found = False

        #     for j in range(len(s)):

        #         if j == i:
        #             continue
                
        #         if s[i] == s[j]:
        #             found= True

        #     if found == False:
        #         return i

        # return -1