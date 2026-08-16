class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        

        # already in sorted order

        i = 0
        j = 0

        n = len(firstList)
        m = len(secondList)

        res = []

        while i < n and j < m:

            s1,e1 = firstList[i]
            s2,e2 = secondList[j]

            # overlapping
            if s2 <= e1 and s1 <= e2:

                # intersection
                s = max(s1,s2)
                e = min(e1,e2)

                res.append([s, e])

            # if interval is over can never intersect with future
            if e1 < e2:
                i += 1
            elif e1 >= e2:
                j += 1

        return res

   










