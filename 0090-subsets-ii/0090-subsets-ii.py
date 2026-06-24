class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        def solve(input, output, res):

            if len(input) == 0 :
                res.add(tuple(output))
                return


            curr_input = input[0]

            input = input[1:]

            solve(input, output, res)

            output.append(curr_input)
            solve(input, output, res)

            output.pop()
            return

        res = set()

        nums.sort()

        solve(nums, [], res)

        return [list(r) for r in res]