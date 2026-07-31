from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:

        # word_map = {}
        # max_ct = -1

        # for c in word:
        #     word_map[c] = word_map.get(c, 0) + 1
        #     if max_ct < word_map[c]:
        #         max_ct = word_map[c]

        # counter = [[] for _ in  range(max_ct+1)]

        # for c, ct in word_map.items():
        #     counter[ct].append(c)

        # multiplier = 1
        # pos = 0
        # cost = 0


        # for i in range(max_ct, 0, -1):

        #     if len(counter[i]) == 0:
        #         continue 

        #     else:
        #         for c in counter[i]:
        #             multiplier = pos // 8 + 1
        #             cost = cost + multiplier * i
        #             pos = pos + 1

        # return cost 

        counts = Counter(word)
        cost = 0
        freqs = sorted(counts.values(), reverse=True)

        for i in range(len(freqs)):

            multiplier = i // 8 + 1

            cost = cost + multiplier * freqs[i]

        return cost