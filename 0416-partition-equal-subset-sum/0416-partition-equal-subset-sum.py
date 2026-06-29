class Solution:

    def subsetSum(self, nums , total):

        t = []
        n = len(nums)

        for i in range(n+1):
            row = []
            for j in range(total+1):

                if j == 0:
                    row.append(True)
                else:
                    row.append(False)
            t.append(row)

        for i in range(1, n+1):
            for j in range(1, total +1):

                if nums[i-1] <= j:

                    c1 = t[i-1][ j - nums[i-1]]
                    c2 = t[i-1][j]
                    t[i][j] = c1 or c2 

                elif nums[i-1] > j:
                    t[i][j] = t[i-1][j]

        return t[n][total]





    def canPartition(self, nums: List[int]) -> bool:

        total = 0

        for n in nums:
            total += n

        if total % 2 != 0:
            return False

        else:

            return self.subsetSum(nums, total//2)     

