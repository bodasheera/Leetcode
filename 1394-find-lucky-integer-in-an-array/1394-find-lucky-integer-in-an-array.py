from collections import Counter
class Solution:


    def findLucky(self, arr: List[int]) -> int:

        count_map = Counter(arr)

        lucky = -1
        for k in count_map:

            if k == count_map[k]:
                lucky = max(lucky, k)

        return lucky


            