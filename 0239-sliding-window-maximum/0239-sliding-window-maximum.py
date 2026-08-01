from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        i = 0
        j = 0
        n = len(nums)
        res = []

        queue = deque()


        while j < n:

            # calculations 
            while queue and queue[-1] < nums[j]:
                    queue.pop()
            queue.append(nums[j])

            # small window size
            if j -i + 1 < k:
                j += 1

            # yo found the window 
            elif j - i + 1 == k:

                # use calc to find ans
                res.append(queue[0])

                # remove ith calculation 
                if queue[0] == nums[i]:
                    queue.popleft()

                # slide the window
                i += 1
                j += 1 



        return res

                

                              

            