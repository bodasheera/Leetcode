class Solution:
    def minimumPushes(self, word: str) -> int:
        

        keys = [0] * 8

        pos = 0 

        for w in word:

            if keys[pos] < 3:
                keys[pos] += 1
                pos += 1
                pos = pos % 8

            else:
                pos += 1
                pos = pos % 8
                keys[pos] += 1
                pos += 1
                pos = pos % 8

        total = 0

        for k in keys:

            total += k * (k+1) // 2

        return total