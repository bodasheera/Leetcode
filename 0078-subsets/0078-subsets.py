class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:

        
        def solve(input, output, arr):

            if len(input) == 0:
                arr.append(output)
                return arr

            op1 = output.copy()
            op2 = output.copy()
            
            op2.append(input[0])

            input = input[1:]

            solve(input, op1, arr)
            solve(input, op2, arr)

        result = []
        solve(nums, [], result)
        return result