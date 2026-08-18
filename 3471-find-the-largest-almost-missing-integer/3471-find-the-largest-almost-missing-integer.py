from collections import defaultdict

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        count = defaultdict(int)

        counter = [0] * 51

        i = 0
        j = 0

        while j < len(nums):
    
            count[nums[j]] = count[nums[j]] + 1


            if j - i + 1 < k:
                j += 1

            elif j - i + 1 == k:


                for c in count:

                    # for all counts of a ele just add 1 
                    if count[c] > 0:
                        counter[c] = counter[c] + 1

                count[nums[i]] = count[nums[i]] - 1
                
                i += 1
                j += 1

            
        for i in range(len(counter)-1 , -1 , -1):
            if counter[i] == 1:
                return i

        return -1

