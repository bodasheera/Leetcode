class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
            counter = [0] * (100 + 1)

            for n in nums:
                counter[n] = counter[n] + 1


            running_sum = [0] * (100 + 1)

            for i in range(1, 101):
                running_sum[i] = counter[i-1] + running_sum[i-1]

            res = []

            for n in nums:
                res.append(running_sum[n])

            return res
