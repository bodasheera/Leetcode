class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i = 0
        j = 0

        check_arr = []

        k = len(needle)

        needle_arr = list(needle)

        while j < len(haystack):

            # calculation
            check_arr.append(haystack[j])

            if j - i + 1 < k:
                j += 1

            # yo found the window
            elif j - i + 1 == k:

                # ans from calculation
                if check_arr == needle_arr:
                    return i
                    
                # remove ith value from calculation
                check_arr.pop(0)

                # slide the window 
                i +=1 
                j += 1

        
        return -1

                
