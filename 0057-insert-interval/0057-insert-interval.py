class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]
        

        # find pos of overlap
        found = -1
        
        # first overlap
        for i in range(len(intervals)):

            s1, e1 = newInterval
            s2, e2 = intervals[i]

            # overlap
            if s1 <= e2 and s2 <= e1:
                
                if s1 < s2:
                    found = i
                else:
                    found = i + 1
                break

            # non overlapping found in between 2 indexes
            elif e1 < s2:
                found = i
                break 

        if found != -1:
            intervals.insert(found, newInterval)
        else:
            intervals.append(newInterval)

        res = [intervals[0]]

        for i in range(1, len(intervals)):

            s1 , e1 = res[-1]
            s2, e2 = intervals[i]

            # overlap
            if e1 >= s2 and e2 >= s1:
                s = min(s1, s2)
                e = max(e1, e2)

                res.pop()
                res.append([s, e])

            else:
                res.append([s2, e2])

        return res


        



