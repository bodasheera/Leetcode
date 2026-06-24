class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        def solve(input, output, res):

            if len(input) == 0 :
                res.add(tuple(output))
                return

            
            op1 = output.copy()
            op2 = output.copy()

            op2.append(input[0])

            input = input[1:]

            solve(input, op1, res)
            solve(input, op2, res)
            return

        res = set()

        nums.sort()

        solve(nums, [], res)

        return [list(r) for r in res]