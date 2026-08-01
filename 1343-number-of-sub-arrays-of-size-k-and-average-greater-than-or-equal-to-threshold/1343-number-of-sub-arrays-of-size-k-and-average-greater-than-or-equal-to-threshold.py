class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        total = 0
        ans = 0

        i = 0
        j = 0

        while j < len(arr):

            # calc 
            total = total + arr[j]
            size_window = j - i + 1
            avg = total / size_window


            # smaller window 
            if size_window < k:
                j += 1

            # yo found the window
            if size_window == k:

                # ans from calc
                if avg >= threshold:
                    ans += 1

                # remove ith calc
                total = total - arr[i]

                # slide the window 
                i += 1
                j += 1

        return ans 