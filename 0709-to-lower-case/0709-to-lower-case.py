class Solution:
    def toLowerCase(self, s: str) -> str:

        res = ""
        
        for i in range(len(s)):
            c = s[i]

            # caps
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                res  += chr(ord(c) + 32 )

            else:
                res += c

        return res

            