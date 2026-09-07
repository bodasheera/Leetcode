class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        place = len(columnTitle) - 1
        base = 26
        res = 0
        for c in columnTitle:
            res += (ord(c) - ord('A') + 1) * (base ** place)
            place -= 1

        return res