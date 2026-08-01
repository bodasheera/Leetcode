from collections import deque

class Solution:
    
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = 0
        all_vowels = ['a', 'e', 'i', 'o', 'u']
        counter = 0
        ans = 0

        while j < len(s):

            # calculation
            if s[j] in all_vowels:
                counter += 1

            # small window
            if j - i + 1 < k:
                j += 1

            # yo found the window 
            elif j - i + 1 == k:

                # ans 
                ans = max(ans , counter)

                # remove ith calc
                if s[i] in all_vowels:
                    counter -= 1

                # slide the window
                i += 1
                j += 1
        
        return ans

    def maxVowelsOld(self, s: str, k: int) -> int:
        
        i = 0
        j = 0
        all_vowels = ['a', 'e', 'i', 'o', 'u']
        found_vowels = deque()
        ans = 0

        while j < len(s):

            # calculation
            if s[j] in all_vowels:
                found_vowels.append(s[j])

            # small window
            if j - i + 1 < k:
                j += 1

            # yo found the window 
            elif j - i + 1 == k:

                # ans 
                ans = max(ans , len(found_vowels))

                # remove ith calc
                if found_vowels and s[i] == found_vowels[0]:
                    found_vowels.popleft()

                # slide the window
                i += 1
                j += 1
        
        return ans



            