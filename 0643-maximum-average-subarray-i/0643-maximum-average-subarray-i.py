class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        

        total = 0
        ans = float('-inf')

        i = 0
        j = 0

        while j < len(nums):

            # calc 
            total = total + nums[j]
            size_window = j - i + 1
            avg = total / size_window


            # smaller window 
            if size_window < k:
                j += 1

            # yo found the window
            if size_window == k:

                # ans from calc
                ans = max(ans , avg)

                # remove ith calc
                total = total - nums[i]

                # slide the window 
                i += 1
                j += 1

        return ans 


