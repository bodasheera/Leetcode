class Solution:
    def romanToInt(self, s: str) -> int:
        
        res = 0

        num_map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C': 100,
            'D': 500,
            'M' : 1000
        }

        i = 0
        while i < len(s):

            if s[i] == 'I' and i+1<len(s) and s[i+1] in ('V', 'X'):
                res = res + num_map[s[i+1]] - num_map[s[i]]
                i += 2

            elif s[i] == 'X' and i+1<len(s) and s[i+1] in ('L', 'C'):
                res = res + num_map[s[i+1]] - num_map[s[i]]
                i += 2

            elif s[i] == 'C' and i+1<len(s) and s[i+1] in ('D', 'M'):
                res = res + num_map[s[i+1]] - num_map[s[i]]
                i += 2
            else:
                res = res + num_map[s[i]]
                i += 1

        return res
