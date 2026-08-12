class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        

        # variable size sliding window
        i = 0
        j = 0
        counter = {}

        res = 0

        while j < len(nums):

            # calculation
            counter[nums[j]] = counter.get(nums[j], 0) + 1

            # condition < k
            # cond = max(counter.values()) commenting as TLE
            cond = counter[nums[j]] # basically only current ele is screwing up our logic 

            # condition < k . valid window
            if cond <= k:
                res = max(res, j - i + 1)
                j += 1

            # invalid condition
            elif cond > k:

                while cond > k:
                    counter[nums[i]] = counter.get(nums[i], 0) - 1
                    i += 1
                    # cond = max(counter.values()) commenting as TLE
                    cond = counter[nums[j]] # basically only current ele is screwing up our logic 

                j += 1
                
        return res
                
