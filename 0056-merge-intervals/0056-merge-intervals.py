class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) <= 1:
            return intervals

        # first step sort it 
        intervals.sort()

        res = [intervals[0]]
        i =1
        
        while i < len(intervals):

            s1, e1 = res[-1]
            s2, e2 = intervals[i]

            # overlapping intervals
            if s2 <= e1 and s1 <= e2:

                # merge intervals
                s = min(s1,s2)
                e = max(e1,e2)

                # merging so remove top of the res
                res.pop()

                # add back the merged interval
                res.append([s,e])

                i += 1
                

            # not overlapping intervals
            elif s1 > e2 or s2 > e1:

                # add the new interval
                res.append(intervals[i])
                i += 1

        return res









