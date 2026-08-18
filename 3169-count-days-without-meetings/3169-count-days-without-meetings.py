class Solution:



    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        # basically GAP

        meetings.sort(key = lambda x: x[0])

        total = 0


        # merge overlapping meetings
        res = [meetings[0]]

        for i in range(1, len(meetings)):
            
            s1, e1 = res[-1]
            s2, e2 = meetings[i]

            # overlapping logic
            if s2 <= e1 and s1 <= e2:
                res.pop()
                s = min(s1, s2)
                e = max(e1, e2)
                res.append([s,e])
            else:
                res.append(meetings[i])

        # now meeting is non overlapping by default
        meetings = res.copy()

        for i in range(1, len(meetings)):

            s1, e1 = meetings[i-1]
            s2, e2 = meetings[i]

            # no overlapping
            # if s2 > e1 or s1 > e2:
            gap = s2 - e1 - 1
            total += gap

        # last meeting end time 
        last = meetings[-1][1]

        if last < days:
            gap = days - last
            total += gap

        # first meeting start time
        first = meetings[0][0]

        if first > 1:
            gap = first - 1
            total += gap

        return total




        


