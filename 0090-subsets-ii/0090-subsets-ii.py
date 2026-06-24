class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        def solve(index, output, res):

            if index == len(nums) :
                res.add(tuple(output))
                return



            solve(index+1, output, res)

            output.append(nums[index])
            solve(index+1, output, res)

            output.pop()
            return

        res = set()

        nums.sort()

        solve(0, [], res)

        return [list(r) for r in res]